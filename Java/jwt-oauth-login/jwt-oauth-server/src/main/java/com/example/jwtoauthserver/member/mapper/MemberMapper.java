package com.example.jwtoauthserver.member.mapper;

import java.util.List;

import org.mapstruct.Mapper;
import org.mapstruct.ReportingPolicy;

import com.example.jwtoauthserver.member.dto.MemberDto;
import com.example.jwtoauthserver.member.entity.Member;

@Mapper(componentModel = "spring", unmappedTargetPolicy = ReportingPolicy.IGNORE)
public interface MemberMapper {
	MemberDto.Response memberToMemberDtoResponse(Member member);

	List<MemberDto.Response> memberToMemberDtoResponse(List<Member> members);
}