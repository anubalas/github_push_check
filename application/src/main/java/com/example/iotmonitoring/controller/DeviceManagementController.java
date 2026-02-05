package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.service.DeviceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

/**
 * Controller for managing IoT devices.
 */
@RestController
@RequestMapping("/api/devices")
public class DeviceManagementController {

    private final DeviceService deviceService;

    @Autowired
    public DeviceManagementController(DeviceService deviceService) {
        this.deviceService = deviceService;
    }

    /**
     * Register a new device.
     */
    @PostMapping
    public ResponseEntity<DeviceData> registerDevice(@RequestBody DeviceData deviceData) {
        DeviceData createdDevice = deviceService.registerDevice(deviceData);
        return ResponseEntity.ok(createdDevice);
    }

    /**
     * Update an existing device.
     */
    @PutMapping("/{id}")
    public ResponseEntity<DeviceData> updateDevice(@PathVariable UUID id, @RequestBody DeviceData deviceData) {
        DeviceData updatedDevice = deviceService.updateDevice(id, deviceData);
        return ResponseEntity.ok(updatedDevice);
    }

    /**
     * Delete a device.
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteDevice(@PathVariable UUID id) {
        deviceService.deleteDevice(id);
        return ResponseEntity.noContent().build();
    }

    /**
     * Retrieve all devices.
     */
    @GetMapping
    public ResponseEntity<List<DeviceData>> getAllDevices() {
        List<DeviceData> devices = deviceService.getAllDevices();
        return ResponseEntity.ok(devices);
    }
}