package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.service.DeviceService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import java.util.UUID;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

/**
 * Unit tests for DeviceManagementController.
 */
public class DeviceManagementControllerTest {

    @InjectMocks
    private DeviceManagementController deviceManagementController;

    @Mock
    private DeviceService deviceService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test registering a device.
     */
    @Test
    public void testRegisterDevice() {
        DeviceData deviceData = new DeviceData();
        // Set properties of deviceData as needed
        when(deviceService.registerDevice(any(DeviceData.class))).thenReturn(deviceData);
        ResponseEntity<DeviceData> response = deviceManagementController.registerDevice(deviceData);
        assert response.getStatusCode().is2xxSuccessful();
    }

    /**
     * Test updating a device.
     */
    @Test
    public void testUpdateDevice() {
        UUID deviceId = UUID.randomUUID();
        DeviceData deviceData = new DeviceData();
        // Set properties of deviceData as needed
        when(deviceService.updateDevice(any(UUID.class), any(DeviceData.class))).thenReturn(deviceData);
        ResponseEntity<DeviceData> response = deviceManagementController.updateDevice(deviceId, deviceData);
        assert response.getStatusCode().is2xxSuccessful();
    }
}
