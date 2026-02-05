package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.service.JwtService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

/**
 * Unit tests for AuthController.
 */
public class AuthControllerTest {

    @InjectMocks
    private AuthController authController;

    @Mock
    private JwtService jwtService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test login functionality.
     */
    @Test
    public void testLogin() {
        String username = "testUser";
        String password = "testPass";
        String token = "mockToken";
        when(jwtService.generateToken(any())).thenReturn(token);
        ResponseEntity<String> response = authController.login(username, password);
        assert response.getStatusCode().is2xxSuccessful();
    }
}
