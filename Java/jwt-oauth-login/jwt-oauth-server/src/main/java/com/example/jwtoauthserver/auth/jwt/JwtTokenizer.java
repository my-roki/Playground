package com.example.jwtoauthserver.auth.jwt;

import java.nio.charset.StandardCharsets;
import java.security.Key;
import java.util.Calendar;
import java.util.Date;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jws;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.io.Encoders;
import io.jsonwebtoken.security.Keys;
import lombok.Getter;

@Component
public class JwtTokenizer {
	@Getter
	@Value("${jwt.key.secret}")
	private String secretKey;

	@Getter
	@Value("${jwt.access-token-expiration-minutes}")
	private int accessTokenExpirationMinutes;

	@Getter
	@Value("${jwt.refresh-token-expiration-minutes}")
	private int refreshTokenExpirationMinutes;

	/**
	 * 인증된 사용자에게 JWT를 최초로 발급해주기 위한 JWT 생성 메서드입니다.
	 * @param claims claims 인증된 사용자와 관련된 정보.
	 * @param subject JWT에 대한 제목
	 * @param expiration JWT에 대한 만료 기한
	 * @param base64EncodingSecretKey Base64 형식 Secret Key
	 * @return Access token
	 */
	public String generateAccessToken(Map<String, Object> claims, String subject, Date expiration,
		String base64EncodingSecretKey) {

		Key key = getKeyFromBase64EncodingSecretKey(base64EncodingSecretKey);

		return Jwts.builder()
			.setClaims(claims)
			.setSubject(subject)
			.setIssuedAt(Calendar.getInstance().getTime())
			.setExpiration(expiration)
			.signWith(key)
			.compact();
	}

	/**
	 * Access Token이 만료되었을 경우, Access Token을 새로 생성할 수 있게 해주는 Refresh Token을 생성하는 메서드입니다.<br>
	 * Refresh Token의 경우 Access Token을 새로 발급해주는 역할을 하는 Token이기 때문에 별도의 Custom Claims는 추가할 필요가 없습니다.
	 * @param subject JWT에 대한 제목
	 * @param expiration JWT에 대한 만료 기한
	 * @param base64EncodingSecretKey Base64 형식 Secret Key
	 * @return Refresh token
	 */
	public String generateRefreshToken(String subject, Date expiration, String base64EncodingSecretKey) {
		Key key = getKeyFromBase64EncodingSecretKey(base64EncodingSecretKey);

		return Jwts.builder()
			.setSubject(subject)
			.setIssuedAt(Calendar.getInstance().getTime())
			.setExpiration(expiration)
			.signWith(key)
			.compact();
	}

	public Jws<Claims> getClaims(String jws, String base64EncodedSecretKey) {
		Key key = getKeyFromBase64EncodingSecretKey(base64EncodedSecretKey);

		Jws<Claims> claims = Jwts.parserBuilder()
			.setSigningKey(key)
			.build()
			.parseClaimsJws(jws);

		return claims;
	}

	/**
	 * JWT의 만료 일시를 지정하기 위한 메서드입니다.
	 * @param expirationMinutes 만료 시간
	 * @return Date 타입의 만료 시간
	 */
	public Date getTokenExpiration(int expirationMinutes) {
		Calendar calendar = Calendar.getInstance();
		calendar.add(Calendar.MINUTE, expirationMinutes);

		Date expiration = calendar.getTime();

		return expiration;
	}

	/**
	 * Plain Text 형태인 Secret Key의 byte[]를 Base64 형식의 문자열로 인코딩 하는 메서드.<br>
	 * jjwt에서 Plain Text 자체를 Secret Key로 사용하는 것은 암호학(cryptographic)적인 작업에 사용되는 Key가 항상 바이너리(byte array)라는 사실과 맞지 않는 것을 감안하여 Plain Text 자체를 Secret Key로 사용하는 것을 권장하지 않고 있습니다.
	 * @param secretKey Plain Text 형태인 Secret Key
	 * @return Base64 형식 Secret Key
	 */
	public String getBase64EncodingSecretKeyFromSecretKey(String secretKey) {
		return Encoders.BASE64.encode(secretKey.getBytes(StandardCharsets.UTF_8));
	}

	/**
	 * JWT의 서명에 사용할 Secret Key를 생성하는 메서드입니다.
	 * @param base64EncodingSecretKey Base64 형식 Secret Key
	 * @return HMAC 알고리즘을 적용한 Key 객체
	 */
	private Key getKeyFromBase64EncodingSecretKey(String base64EncodingSecretKey) {
		byte[] bytes = Decoders.BASE64.decode(base64EncodingSecretKey);
		Key key = Keys.hmacShaKeyFor(bytes);

		return key;
	}
}
