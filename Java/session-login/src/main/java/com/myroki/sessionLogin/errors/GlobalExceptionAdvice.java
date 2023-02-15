package com.myroki.sessionLogin.errors;

import static com.myroki.sessionLogin.utils.ApiUtils.*;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestControllerAdvice
public class GlobalExceptionAdvice {
	@ExceptionHandler(CustomException.class)
	public ResponseEntity<?> handleCustomException(CustomException exception) {
		log.error("Custom exception occurred: {}", exception.getMessage(), exception);
		return new ResponseEntity<>(error(exception, HttpStatus.valueOf(exception.getExceptionCode().getStatus())),
			HttpStatus.valueOf(exception.getExceptionCode().getStatus()));
	}
}

