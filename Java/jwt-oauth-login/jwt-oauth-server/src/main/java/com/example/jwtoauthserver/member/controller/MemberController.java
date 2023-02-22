package com.example.jwtoauthserver.member.controller;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.jwtoauthserver.member.dto.MemberDto;
import com.example.jwtoauthserver.member.entity.Member;
import com.example.jwtoauthserver.member.mapper.MemberMapper;
import com.example.jwtoauthserver.member.service.MemberService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/v1/members")
@RequiredArgsConstructor
public class MemberController {

	private final MemberService memberService;
	private final MemberMapper mapper;

	@GetMapping
	public ResponseEntity<?> getAllMembers() {

		List<Member> members = memberService.findAllMembers();
		List<MemberDto.Response> responses = mapper.memberToMemberDtoResponse(members);

		return new ResponseEntity<>(responses, HttpStatus.OK);
	}
}
