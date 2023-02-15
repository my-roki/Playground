package com.myroki.sessionLogin.auth.controller;

import static com.myroki.sessionLogin.utils.ApiUtils.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.myroki.sessionLogin.auth.dto.AuthDto;
import com.myroki.sessionLogin.auth.entity.Member;
import com.myroki.sessionLogin.auth.service.AuthService;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestController
@RequestMapping("/api/v1/auth")
@RequiredArgsConstructor
public class AuthController {
	private final AuthService authService;

	@PostMapping("/signup")
	public ResponseEntity<?> signup(@RequestBody AuthDto.Signup request) {

		authService.signup(request);

		return new ResponseEntity<>(success(true), HttpStatus.CREATED);
	}

	@PostMapping("/login")
	public ResponseEntity<?> login(@RequestBody AuthDto.Login request,
		HttpServletResponse response) {
		String username = request.getUsername();
		String password = request.getPassword();

		Member member = authService.login(username, password);
		String greeting = "Hello " + username;

		Cookie cookie = new Cookie("memberId", String.valueOf(member.getId()));
		response.addCookie(cookie);
		log.info("쿠키 생성 완료 : {}", cookie);

		return new ResponseEntity<>(success(greeting), HttpStatus.OK);
	}

	@GetMapping("/me")
	public ResponseEntity<?> aboutMe(@CookieValue(name = "memberId", required = false) Long memberId) {
		if (memberId == null) {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}

		Member member = authService.findMe(memberId);
		String result = "I think you are " + member.getUsername();

		return new ResponseEntity<>(success(result), HttpStatus.ACCEPTED);
	}

	@PostMapping("/logout")
	public ResponseEntity<?> logout(HttpServletResponse response) {
		Cookie cookie = new Cookie("memberId", null);
		cookie.setMaxAge(0);
		response.addCookie(cookie);
		log.info("쿠키 삭제 완료 : {}", cookie);

		return new ResponseEntity<>(success(true), HttpStatus.OK);
	}
}
