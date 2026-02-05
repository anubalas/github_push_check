package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.DeviceData;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

/**
 * Repository interface for managing time-series data from devices.
 */
@Repository
public interface DeviceDataRepository extends JpaRepository<DeviceData, UUID> {
    // Custom query methods for time-series data can be added here
    List<DeviceData> findByDeviceId(UUID deviceId);
}