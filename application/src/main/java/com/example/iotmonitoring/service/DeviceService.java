package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.repository.DeviceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;

/**
 * Service for managing IoT devices.
 */
@Service
public class DeviceService {

    /**
     * Repository for accessing device data.
     */
    private final DeviceRepository deviceRepository;

    @Autowired
    public DeviceService(final DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    /**
     * Register a new device.
     * @param deviceData The device data to register.
     * @return The registered device data.
     */
    public DeviceData registerDevice(final DeviceData deviceData) {
        return deviceRepository.save(deviceData);
    }

    /**
     * Update an existing device.
     * @param id The ID of the device to update.
     * @param deviceData The new device data.
     * @return The updated device data.
     */
    public DeviceData updateDevice(final UUID id, final DeviceData deviceData) {
        deviceData.setId(id);
        return deviceRepository.save(deviceData);
    }

    /**
     * Delete a device.
     * @param id The ID of the device to delete.
     */
    public void deleteDevice(final UUID id) {
        deviceRepository.deleteById(id);
    }

    /**
     * Retrieve all devices.
     * @return A list of all device data.
     */
    public List<DeviceData> getAllDevices() {
        return deviceRepository.findAll();
    }
}