package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.service.DataProcessingService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import static org.mockito.Mockito.when;

/**
 * Unit tests for DataProcessingController.
 */
public class DataProcessingControllerTest {

    @InjectMocks
    private DataProcessingController dataProcessingController;

    @Mock
    private DataProcessingService dataProcessingService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test processing data.
     */
    @Test
    public void testProcessData() {
        String rawData = "{\"key\":\"value\"}"; // Example JSON data
        when(dataProcessingService.validateDataFormat(rawData)).thenReturn(true);
        ResponseEntity<String> response = dataProcessingController.processData(rawData);
        assert response.getStatusCode().is2xxSuccessful();
    }
}
