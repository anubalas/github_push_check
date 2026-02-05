package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.service.DataQueryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

/**
 * Controller for querying device data.
 */
@RestController
@RequestMapping("/api/data")
public class DataQueryController {

    private final DataQueryService dataQueryService;

    @Autowired
    public DataQueryController(DataQueryService dataQueryService) {
        this.dataQueryService = dataQueryService;
    }

    /**
     * Retrieve historical data for a specific device.
     */
    @GetMapping("/{deviceId}")
    public ResponseEntity<List<DeviceData>> getDeviceData(@PathVariable UUID deviceId) {
        List<DeviceData> data = dataQueryService.getDeviceData(deviceId);
        return ResponseEntity.ok(data);
    }
}