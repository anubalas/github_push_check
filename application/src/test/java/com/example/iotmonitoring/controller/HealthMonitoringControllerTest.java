package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.service.HealthMonitoringService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import java.util.UUID;

import static org.mockito.Mockito.when;

/**
 * Unit tests for HealthMonitoringController.
 */
public class HealthMonitoringControllerTest {

    @InjectMocks
    private HealthMonitoringController healthMonitoringController;

    @Mock
    private HealthMonitoringService healthMonitoringService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test getting device health status.
     */
    @Test
    public void testGetDeviceHealth() {
        UUID deviceId = UUID.randomUUID();
        DeviceData deviceData = new DeviceData();
        when(healthMonitoringService.getDeviceHealth(deviceId)).thenReturn(deviceData);
        ResponseEntity<DeviceData> response = healthMonitoringController.getDeviceHealth(deviceId);
        assert response.getStatusCode().is2xxSuccessful();
    }
}
