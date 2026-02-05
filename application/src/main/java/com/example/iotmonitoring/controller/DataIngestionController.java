package com.example.iotmonitoring.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import javax.validation.Valid;
import javax.validation.constraints.NotNull;

/**
 * REST controller for handling data ingestion from IoT devices.
 */
@RestController
@RequestMapping("/api/ingest")
public class DataIngestionController {

    /**
     * Accepts JSON data via HTTP POST.
     * 
     * @param data The incoming JSON data.
     * @return ResponseEntity indicating the result of the operation.
     */
    @PostMapping
    public ResponseEntity<String> ingestData(@Valid @RequestBody @NotNull String data) {
        // Validate and process the incoming JSON data
        // TODO: Add data processing logic here
        return new ResponseEntity<>("Data ingested successfully", HttpStatus.OK);
    }
}