package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.AlertRule;
import com.example.iotmonitoring.service.AlertService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.UUID;

/**
 * Controller for managing alert rules and triggering alerts.
 */
@RestController
@RequestMapping("/api/alerts")
public class AlertController {

    private final AlertService alertService;

    @Autowired
    public AlertController(AlertService alertService) {
        this.alertService = alertService;
    }

    /**
     * Define a new alert rule.
     * @param alertRule The alert rule to be defined.
     * @return ResponseEntity indicating the result of the operation.
     */
    @PostMapping
    public ResponseEntity<Void> defineAlertRule(@RequestBody AlertRule alertRule) {
        alertService.defineAlertRule(alertRule);
        return ResponseEntity.ok().build();
    }

    /**
     * Monitor incoming data and trigger alerts if necessary.
     * @param deviceId The ID of the device.
     * @param data The incoming data to be monitored.
     * @return ResponseEntity indicating the result of the operation.
     */
    @PostMapping("/monitor/{deviceId}")
    public ResponseEntity<Void> monitorData(@PathVariable UUID deviceId, @RequestBody Object data) {
        alertService.monitorData(deviceId, data);
        return ResponseEntity.ok().build();
    }
}