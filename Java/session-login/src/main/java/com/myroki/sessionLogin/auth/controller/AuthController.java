package com.myroki.sessionLogin.auth.controller;

import static com.myroki.sessionLogin.utils.ApiUtils.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.SessionAttribute;

import com.myroki.sessionLogin.auth.dto.AuthDto;
import com.myroki.sessionLogin.auth.entity.Member;
import com.myroki.sessionLogin.auth.service.AuthService;
import com.myroki.sessionLogin.utils.ApplicationConstant;
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
	public ResponseEntity<?> login(@RequestBody AuthDto.Login body, HttpServletRequest request) {
		String username = body.getUsername();
		String password = body.getPassword();

		Member member = authService.login(username, password);
		String greeting = "Hello " + username;

		// 이미 로그인한 사용자라면 이전 로그인은 무효합니다.
		sessionManager.getSessionCheck(member.getId());

		// sessionStore에 member 객체를 저장합니다.
		HttpSession session = request.getSession();
		session.setAttribute(ApplicationConstant.LOGIN_MEMBER, member);

		return new ResponseEntity<>(success(greeting), HttpStatus.OK);
	}

	@GetMapping("/me")
	public ResponseEntity<?> aboutMe(
		@SessionAttribute(name = ApplicationConstant.LOGIN_MEMBER, required = false) Member loginMember) {
		if (loginMember == null) {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}

		Member member = authService.findMe(loginMember.getId());
		String result = "I think you are " + member.getUsername();

		return new ResponseEntity<>(success(result), HttpStatus.ACCEPTED);
	}

	@PostMapping("/logout")
	public ResponseEntity<?> logout(HttpServletRequest request) {

		HttpSession session = request.getSession(false);
		if (session != null) {
			session.invalidate();
		}
		return new ResponseEntity<>(success(true), HttpStatus.OK);
	}
}
