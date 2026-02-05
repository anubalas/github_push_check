package com.example.iotmonitoring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Main application class for the IoT Monitoring Microservice.
 * This class serves as the entry point for the application.
 */
@SpringBootApplication
public class IotMonitoringApplication {

    /**
     * The main method that starts the IoT Monitoring Microservice.
     * 
     * @param args Command line arguments passed during application startup.
     */
    public static void main(String[] args) {
        SpringApplication.run(IotMonitoringApplication.class, args);
    }
}