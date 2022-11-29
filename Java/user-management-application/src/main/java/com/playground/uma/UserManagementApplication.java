package com.playground.uma;

import com.playground.uma.entity.User;
import com.playground.uma.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class UserManagementApplication implements CommandLineRunner {
	@Autowired
	private UserRepository userRepository;


	public static void main(String[] args) {
		SpringApplication.run(UserManagementApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		User roki = new User("roki", "my", "my_roki@hello.com");
		User toki = new User("toki", "your", "your_toki@hello.com");
		User poki = new User("poki", "our", "our_poki@hello.com");

		userRepository.save(roki);
		userRepository.save(toki);
		userRepository.save(poki);
	}
}
