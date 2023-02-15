package com.myroki.sessionLogin.errors;

import lombok.Getter;

@Getter
public class CustomException extends RuntimeException {
	private final ExceptionCode exceptionCode;
	private final String message;

	public CustomException(ExceptionCode exceptionCode, String message) {
		this.exceptionCode = exceptionCode;
		this.message = message != null ? message : exceptionCode.getMessage();
	}
}
