package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.repository.DeviceDataRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;

/**
 * Service for querying device data.
 */
@Service
public class DataQueryService {

    private final DeviceDataRepository deviceDataRepository;

    @Autowired
    public DataQueryService(DeviceDataRepository deviceDataRepository) {
        this.deviceDataRepository = deviceDataRepository;
    }

    /**
     * Retrieve historical data for a specific device.
     */
    public List<DeviceData> getDeviceData(UUID deviceId) {
        return deviceDataRepository.findByDeviceId(deviceId);
    }
}