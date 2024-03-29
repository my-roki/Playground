package com.myroki.sessionLogin.utils;

import java.util.Arrays;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Component;

import com.myroki.sessionLogin.auth.entity.Member;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@Component
public class SessionManager {
	public static final String SESSION_COOKIE_NAME = "sessionId";

	// 동시성 문제가 있는 경우 ConcurrentHashMap 를 사용해 문제를 해결합니다.
	private final Map<String, Object> sessionStore = new ConcurrentHashMap<>();

	/**
	 * 세션을 생성합니다. <br>
	 * 랜덤으로 생성된 세션 아이디와 보관할 값을 sessionStore에 저장합니다. <br>
	 * 쿠키에 세션 id를 담아 응답으로 전달합니다.
	 * @param response 세션 id가 담긴 쿠키를 저장할 응답
	 * @param value sessionStore에 저장항 객체 정보
	 */
	public Cookie createSession(HttpServletResponse response, Object value) {
		String sessionId = UUID.randomUUID().toString();
		sessionStore.put(sessionId, value);

		Cookie cookie = new Cookie(SESSION_COOKIE_NAME, sessionId);
		response.addCookie(cookie);

		log.info("로그인 후 현재 sessionStore 상태 {}", sessionStore);
		return cookie;
	}

	/**
	 * 들어온 쿠키 안에서 세션에 해당되는 값을 찾아 sessoinStore에저장되어 있는 데이터를 조회합니다.
	 * @param request 쿠키가 담겨있는 요청
	 * @return sessionStore에 저장되어 있는 데이터값
	 */
	public Object getSession(HttpServletRequest request) {
		// SessionCookie 에 findCookie 를 메서드를 사용해서 찾아온 SESSION_COOKIE_NAME 를 저장함
		Cookie cookie = findCookie(request, SESSION_COOKIE_NAME);
		if (cookie == null) {
			return null;
		}
		return sessionStore.get(cookie.getValue());
	}

	/**
	 * 요청에서 쿠키 이름으로 원하는 쿠키를 찾습니다.
	 * @param request 쿠키를 찾을 요청
	 * @param cookieName 찾고싶은 쿠키의 이름
	 * @return 요청 속에 원하는 쿠키 데이터가 있으면 쿠키를 반환합니다.
	 */
	public Cookie findCookie(HttpServletRequest request, String cookieName) {
		Cookie[] cookies = request.getCookies();

		if (cookies == null) {
			return null;
		}

		return Arrays.stream(cookies)
			.filter(cookie -> cookie.getName().equals(cookieName))
			.findAny()
			.orElse(null);
	}

	/**
	 * 쿠키에 로그인 정보(세션 id)가 있다면 파기합니다.
	 * @param request 쿠키를 찾을 요청
	 * @return 세션이 만료된 쿠키
	 */
	public Cookie expireCookie(HttpServletRequest request) {
		Cookie cookie = findCookie(request, SESSION_COOKIE_NAME);

		if (cookie != null) {
			sessionStore.remove(cookie.getValue());
		}

		log.info("로그아웃 후 현재 sessionStore 상태 {}", sessionStore);
		return cookie;
	}

	/**
	 * 같은 아이디로 여러번 로그인시 sessionStore에 있는 이전 데이터를 삭제합니다.
	 * @param memberId 중복 로그인을 체크할 id
	 */
	public synchronized void getSessionCheck(Long memberId) {
		for (String key : sessionStore.keySet()) {
			Member member = (Member)sessionStore.get(key);
			if (member != null && member.getId().equals(memberId)) {
				sessionStore.remove(key);
			}
		}
	}
}

