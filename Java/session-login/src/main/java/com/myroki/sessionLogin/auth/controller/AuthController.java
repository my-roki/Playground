package com.myroki.sessionLogin.auth.controller;

import static com.myroki.sessionLogin.utils.ApiUtils.*;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.myroki.sessionLogin.auth.dto.AuthDto;
import com.myroki.sessionLogin.auth.service.AuthService;

import lombok.RequiredArgsConstructor;

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

}
