package com.playground.uma.service;

import com.playground.uma.entity.User;
import com.playground.uma.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserServiceImp implements UserService {
    private final UserRepository userRepository;

    public UserServiceImp(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public List<User> getAllUSer() {
        return userRepository.findAll();
    }

    @Override
    public User createUser(User user) {
        return userRepository.save(user);
    }

    @Override
    public User updateUser(User user) {
        User findUser = findUserById(user.getId());
        findUser.setFirstName(user.getFirstName());
        findUser.setLastName(user.getLastName());
        findUser.setEmail(user.getEmail());

        return userRepository.save(findUser);
    }

    @Override
    public void deleteUserById(Long id) {
        findUserById(id);
        userRepository.deleteById(id);
    }

    @Override
    public User findUserById(Long id) {
        Optional<User> optionalUser = userRepository.findById(id);
        User user = optionalUser.orElseThrow(() -> {
            throw new RuntimeException();
        });

        return user;
    }



}