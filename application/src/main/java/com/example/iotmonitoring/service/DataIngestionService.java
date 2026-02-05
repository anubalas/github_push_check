package com.example.iotmonitoring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.EnableCaching;
import com.example.iotmonitoring.repository.DeviceDataRepository;
import com.example.iotmonitoring.model.DeviceData;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.ArrayList;
import java.util.UUID;

/**
 * Service for handling data ingestion from IoT devices.
 * Implements batching for high throughput data ingestion and caching for frequently accessed data.
 */
@Service
@EnableCaching
public class DataIngestionService {
    private final DeviceDataRepository deviceDataRepository;
    private final BlockingQueue<DeviceData> dataQueue;
    private final int BATCH_SIZE = 100;

    @Autowired
    public DataIngestionService(DeviceDataRepository deviceDataRepository) {
        this.deviceDataRepository = deviceDataRepository;
        this.dataQueue = new LinkedBlockingQueue<>();
        startBatchProcessing();
    }

    /**
     * Method to ingest data from IoT devices.
     * @param deviceData The data to be ingested.
     */
    public void ingestData(DeviceData deviceData) {
        dataQueue.offer(deviceData);
    }

    /**
     * Starts a background thread to process data in batches.
     */
    private void startBatchProcessing() {
        new Thread(() -> {
            while (true) {
                try {
                    List<DeviceData> batch = new ArrayList<>();
                    dataQueue.drainTo(batch, BATCH_SIZE);
                    if (!batch.isEmpty()) {
                        deviceDataRepository.saveAll(batch);
                    }
                } catch (Exception e) {
                    // Handle exceptions appropriately
                }
            }
        }).start();
    }

    /**
     * Caches frequently accessed device data.
     * @param deviceId The ID of the device.
     * @return List of device data.
     */
    @Cacheable(value = "deviceDataCache", key = "#deviceId")
    public List<DeviceData> getDeviceData(UUID deviceId) {
        return deviceDataRepository.findByDeviceId(deviceId);
    }
}