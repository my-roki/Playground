package com.myroki.sessionLogin.auth.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

public class AuthDto {

	@Setter
	@Getter
	@NoArgsConstructor
	public static class Signup {
		private String username;
		private String password;
		private String passwordConfirm;
	}

	@Setter
	@Getter
	@NoArgsConstructor
	public static class Login {
		private String username;
		private String password;
	}
}
