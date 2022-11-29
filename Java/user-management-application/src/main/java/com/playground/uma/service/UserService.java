package com.playground.uma.service;

import com.playground.uma.entity.User;

import java.util.List;

public interface UserService {
    List<User> getAllUSer();

    User createUser(User user);

    User updateUser(User user);

    User findUserById(Long id);

    void deleteUserById(Long id);
}