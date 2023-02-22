package com.example.jwtoauthserver.member.entity;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Getter;

@Getter
@Entity(name = "MEMBERS")
public class Member {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long memberId;

	@Column(nullable = false, unique = true, updatable = false)
	private String email;

	@Column(nullable = false, length = 32)
	private String username;

	@ElementCollection(fetch = FetchType.EAGER)
	private List<String> roles = new ArrayList<>();
}
