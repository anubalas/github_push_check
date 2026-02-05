package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.DeviceData;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.UUID;

/**
 * Repository interface for managing device metadata.
 */
@Repository
public interface DeviceRepository extends JpaRepository<DeviceData, UUID> {
    // Additional query methods can be defined here if needed
}
