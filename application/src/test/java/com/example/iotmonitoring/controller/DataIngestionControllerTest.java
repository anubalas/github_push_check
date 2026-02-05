package com.example.iotmonitoring.controller;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.http.ResponseEntity;
import org.mockito.InjectMocks;
import org.mockito.MockitoAnnotations;

import static org.mockito.Mockito.when;

/**
 * Unit tests for DataIngestionController.
 */
public class DataIngestionControllerTest {

    @InjectMocks
    private DataIngestionController dataIngestionController;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test ingesting data.
     */
    @Test
    public void testIngestData() {
        String jsonData = "{\"key\":\"value\"}"; // Example JSON data
        ResponseEntity<String> response = dataIngestionController.ingestData(jsonData);
        assert response.getStatusCode().is2xxSuccessful();
    }
}
