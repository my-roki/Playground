package com.example.jwtoauthserver.member.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.jwtoauthserver.member.entity.Member;

public interface MemberRepository extends JpaRepository<Member, Long> {
}
