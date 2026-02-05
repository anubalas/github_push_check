package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.service.HealthMonitoringService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

/**
 * Controller for health monitoring of devices.
 */
@RestController
@RequestMapping("/api/health")
public class HealthMonitoringController {

    private final HealthMonitoringService healthMonitoringService;

    @Autowired
    public HealthMonitoringController(HealthMonitoringService healthMonitoringService) {
        this.healthMonitoringService = healthMonitoringService;
    }

    /**
     * Get the health status of a device.
     */
    @GetMapping("/{deviceId}")
    public ResponseEntity<DeviceData> getDeviceHealth(@PathVariable UUID deviceId) {
        DeviceData healthStatus = healthMonitoringService.getDeviceHealth(deviceId);
        return ResponseEntity.ok(healthStatus);
    }
}