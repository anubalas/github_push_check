package com.example.iotmonitoring.model;

import javax.persistence.*;
import java.util.UUID;

/**
 * Entity class representing time-series data from devices.
 */
@Entity
@Table(name = "device_data")
public class DeviceData {
    @Id
    @GeneratedValue
    private UUID id;
    @Column(name = "device_id")
    private UUID deviceId;
    private java.sql.Timestamp timestamp;
    private String data;
    private java.sql.Timestamp createdAt;

    // Getters and Setters
    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public UUID getDeviceId() {
        return deviceId;
    }

    public void setDeviceId(UUID deviceId) {
        this.deviceId = deviceId;
    }

    public java.sql.Timestamp getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(java.sql.Timestamp timestamp) {
        this.timestamp = timestamp;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public java.sql.Timestamp getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(java.sql.Timestamp createdAt) {
        this.createdAt = createdAt;
    }
}
