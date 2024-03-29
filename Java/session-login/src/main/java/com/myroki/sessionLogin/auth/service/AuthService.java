package com.myroki.sessionLogin.auth.service;

import static lombok.Lombok.*;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.myroki.sessionLogin.auth.dto.AuthDto;
import com.myroki.sessionLogin.auth.entity.Member;
import com.myroki.sessionLogin.auth.repository.MemberRepository;
import com.myroki.sessionLogin.errors.CustomException;
import com.myroki.sessionLogin.errors.ExceptionCode;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class AuthService {
	private final MemberRepository memberRepository;

	public void signup(AuthDto.Signup request) {
		checkNotNull(request, "request must be provided");

		String username = request.getUsername();
		String password = request.getPassword();

		if (existMemberByUsername(username)) {
			throw new CustomException(ExceptionCode.ALREADY_EXIST, "Username " + username + " already exist.");
		}

		if (!password.equals(request.getPasswordConfirm())) {
			throw new RuntimeException("Password does not matches.");
		}

		// Password encryption is required.
		Member member = new Member(username, password);
		memberRepository.save(member);
	}

	public Member login(String username, String password) {
		Member member = findMemberByUsername(username);

		if (!password.equals(member.getPassword())) {
			throw new CustomException(ExceptionCode.WRONG_PASSWORD, null);
		}

		return member;
	}

	public Member findMe(Long memberId) {
		Optional<Member> optionalMember = memberRepository.findById(memberId);

		return optionalMember.orElseThrow(
			() -> new CustomException(ExceptionCode.NOT_FOUND, "Could not found user"));
	}

	public Boolean existMemberByUsername(String username) {
		Optional<Member> optionalMember = memberRepository.findByUsername(username);
		return optionalMember.isPresent();
	}

	public Member findMemberByUsername(String username) {
		Optional<Member> optionalMember = memberRepository.findByUsername(username);
		return optionalMember.orElseThrow(
			() -> new CustomException(ExceptionCode.NOT_FOUND, "Could not found user for " + username));
	}
}
