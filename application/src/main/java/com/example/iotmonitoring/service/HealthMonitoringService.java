package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.repository.DeviceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.UUID;

/**
 * Service for health monitoring of devices.
 */
@Service
public class HealthMonitoringService {

    /**
     * Repository for accessing device data.
     */
    private final DeviceRepository deviceRepository;

    @Autowired
    public HealthMonitoringService(final DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    /**
     * Get the health status of a device.
     * @param deviceId The ID of the device to check.
     * @return The health status of the device.
     */
    public DeviceData getDeviceHealth(final UUID deviceId) {
        return deviceRepository.findById(deviceId).orElse(null);
    }
}