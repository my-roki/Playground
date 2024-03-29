package com.example.jwtoauthserver.auth.handler;

import java.io.IOException;
import java.net.URI;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.security.core.Authentication;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.security.web.authentication.SimpleUrlAuthenticationSuccessHandler;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.util.UriComponentsBuilder;

import com.example.jwtoauthserver.auth.jwt.JwtTokenizer;
import com.example.jwtoauthserver.auth.utils.CustomAuthorityUtils;
import com.example.jwtoauthserver.member.entity.Member;
import com.example.jwtoauthserver.member.service.MemberService;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class OAuth2MemberSuccessHandler extends SimpleUrlAuthenticationSuccessHandler {
	private final JwtTokenizer jwtTokenizer;
	private final CustomAuthorityUtils authorityUtils;
	private final MemberService memberService;

	public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response,
		Authentication authentication) throws IOException {
		OAuth2User oAuth2User = (OAuth2User)authentication.getPrincipal();
		String email = String.valueOf(oAuth2User.getAttributes().get("email"));

		List<String> authorities = authorityUtils.createRoles(email);

		saveMember(email);
		redirect(request, response, email, authorities);
	}

	private void saveMember(String email) {
		Member member = new Member();
		member.setEmail(email);
		memberService.createMember(member);
	}

	private void redirect(HttpServletRequest request, HttpServletResponse response, String username,
		List<String> authorities) throws
		IOException {
		String accessToken = delegateAccessToken(username, authorities);
		String refreshToken = delegateRefreshToken(username);

		String uri = createURI(accessToken, refreshToken).toString();
		getRedirectStrategy().sendRedirect(request, response, uri);
	}

	private String delegateAccessToken(String username, List<String> authorities) {
		Map<String, Object> claims = new HashMap<>();
		claims.put("username", username);
		claims.put("roles", authorities);

		String subject = username;
		Date expiration = jwtTokenizer.getTokenExpiration(jwtTokenizer.getAccessTokenExpirationMinutes());

		String base64EncodedSecretKey = jwtTokenizer.getBase64EncodingSecretKeyFromSecretKey(
			jwtTokenizer.getSecretKey());

		String accessToken = jwtTokenizer.generateAccessToken(claims, subject, expiration, base64EncodedSecretKey);

		return accessToken;
	}

	private String delegateRefreshToken(String username) {
		String subject = username;
		Date expiration = jwtTokenizer.getTokenExpiration(jwtTokenizer.getRefreshTokenExpirationMinutes());
		String base64EncodedSecretKey = jwtTokenizer.getBase64EncodingSecretKeyFromSecretKey(
			jwtTokenizer.getSecretKey());

		String refreshToken = jwtTokenizer.generateRefreshToken(subject, expiration, base64EncodedSecretKey);

		return refreshToken;
	}

	private URI createURI(String accessToken, String refreshToken) {
		MultiValueMap<String, String> queryParams = new LinkedMultiValueMap<>();
		queryParams.add("access_token", accessToken);
		queryParams.add("refresh_token", refreshToken);

		return UriComponentsBuilder
			.newInstance()
			.scheme("http")
			.host("localhost")
			.port(3000)
			.path("/oauth/redirect")
			.queryParams(queryParams)
			.build()
			.toUri();
	}

}
