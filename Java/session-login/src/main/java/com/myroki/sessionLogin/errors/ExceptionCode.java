package com.myroki.sessionLogin.errors;

import lombok.AllArgsConstructor;
import lombok.Getter;

/**
 * status - Http status code. <br>
 * message - 에러 내용 에 관한 구체적인 메세지를 작성합니다.
 */
@Getter
@AllArgsConstructor
public enum ExceptionCode {
	NOT_FOUND(404, "Contents not found."),
	ALREADY_EXIST(409, "Contents already exist."),
	WRONG_PASSWORD(409, "Password does not matches." );

	private final int status;
	private final String message;
}
