package com.myroki.sessionLogin.auth.controller;

import static com.myroki.sessionLogin.utils.ApiUtils.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.myroki.sessionLogin.auth.dto.AuthDto;
import com.myroki.sessionLogin.auth.entity.Member;
import com.myroki.sessionLogin.auth.service.AuthService;
import com.myroki.sessionLogin.utils.SessionManager;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestController
@RequestMapping("/api/v1/auth")
@RequiredArgsConstructor
public class AuthController {
	private final AuthService authService;
	private final SessionManager sessionManager;

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

		// sessionStore에 member 객체를 저장합니다.
		Cookie cookie = sessionManager.createSession(response, member);
		log.info("쿠키 생성 완료 : {}", cookie);

		return new ResponseEntity<>(success(greeting), HttpStatus.OK);
	}

	@GetMapping("/me")
	public ResponseEntity<?> aboutMe(HttpServletRequest request) {
		// sessionStore에 저장되어 있던 Member 정보를 가져옵니다.
		Member sessionMember = (Member)sessionManager.getSession(request);

		if (sessionMember == null) {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}

		Member member = authService.findMe(sessionMember.getId());
		String result = "I think you are " + member.getUsername();

		return new ResponseEntity<>(success(result), HttpStatus.ACCEPTED);
	}

	@PostMapping("/logout")
	public ResponseEntity<?> logout(HttpServletRequest request) {

		// sessionStore에 저장되어 있던 세션 정보를 파기합니다.
		Cookie cookie = sessionManager.expireCookie(request);
		log.info("쿠키 삭제 완료 : {}", cookie);

		return new ResponseEntity<>(success(true), HttpStatus.OK);
	}
}
