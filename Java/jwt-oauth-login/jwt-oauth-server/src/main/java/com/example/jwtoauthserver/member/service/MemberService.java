package com.example.jwtoauthserver.member.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.jwtoauthserver.member.entity.Member;
import com.example.jwtoauthserver.member.repository.MemberRepository;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class MemberService {
	private final MemberRepository memberRepository;

	public List<Member> findAllMembers() {
		return memberRepository.findAll();

	}
}
