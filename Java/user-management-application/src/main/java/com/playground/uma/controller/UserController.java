package com.playground.uma.controller;

import com.playground.uma.entity.User;
import com.playground.uma.service.UserService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    // Handler methods
    @GetMapping("/users")
    public String getUsers(Model model) {
        model.addAttribute("users", userService.getAllUSer());

        return "users";
    }

    @GetMapping("/users/new")
    public String createUserForm(Model model) {
        User user = new User();
        model.addAttribute("user", user);
        return "create_user";
    }

    @PostMapping("/users")
    public String postUser(@ModelAttribute("users") User user) {
        userService.createUser(user);
        return "redirect:/users";
    }

    @GetMapping("/users/edit/{id}")
    public String editUserForm(@PathVariable Long id, Model model) {
        model.addAttribute("user", userService.findUserById(id));
        return "edit_user";

    }

    @PatchMapping("/users/{id}")
    public String patchUser(@PathVariable Long id, @ModelAttribute("user") User user, Model model) {
        userService.updateUser(user);
        return "redirect:/users";
    }

    @GetMapping("/users/delete/{id}")
    public String deleteUser(@PathVariable Long id) {
        userService.deleteUserById(id);
        return "redirect:/users";
    }
}