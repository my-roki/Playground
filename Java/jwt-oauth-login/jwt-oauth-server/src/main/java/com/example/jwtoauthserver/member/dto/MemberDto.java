package com.example.jwtoauthserver.member.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

public class MemberDto {

	@Getter
	@Setter
	@NoArgsConstructor
	public static class Response {
		private Long memberId;
		private String email;
		private String username;
	}
}
