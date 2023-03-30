package com.example.jwtoauthserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.PropertySource;

@SpringBootApplication
@PropertySource(value = "classpath:/env.properties", ignoreResourceNotFound = true)
public class JwtOauthServerApplication {

	public static void main(String[] args) {
		SpringApplication.run(JwtOauthServerApplication.class, args);
	}

}
