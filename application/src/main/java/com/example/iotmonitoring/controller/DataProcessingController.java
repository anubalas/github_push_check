package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.service.DataProcessingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * REST controller for processing IoT device data.
 */
@RestController
@RequestMapping("/api/data")
public class DataProcessingController {

    @Autowired
    private DataProcessingService dataProcessingService;

    /**
     * Endpoint to process incoming device data.
     * @param rawData The raw data from the device.
     * @return ResponseEntity with the result of processing.
     */
    @PostMapping
    public ResponseEntity<String> processData(@RequestBody String rawData) {
        try {
            dataProcessingService.validateDataFormat(rawData);
            // Further processing logic
            return ResponseEntity.ok("Data processed successfully.");
        } catch (Exception e) {
            return dataProcessingService.handleError(e);
        }
    }
}