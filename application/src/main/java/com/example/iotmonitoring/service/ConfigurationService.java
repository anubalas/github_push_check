package com.example.iotmonitoring.service;

import org.springframework.stereotype.Service;

/**
 * Service for managing configuration settings for data ingestion intervals.
 */
@Service
public class ConfigurationService {

    /**
     * Default interval for data ingestion in milliseconds.
     */
    private static final long DEFAULT_INGESTION_INTERVAL = 1000;
    private long ingestionInterval = DEFAULT_INGESTION_INTERVAL;

    /**
     * Set the data ingestion interval.
     * 
     * @param interval The new ingestion interval in milliseconds.
     */
    public void setIngestionInterval(final long interval) {
        this.ingestionInterval = interval;
    }

    /**
     * Get the current data ingestion interval.
     * 
     * @return The current ingestion interval in milliseconds.
     */
    public long getIngestionInterval() {
        return ingestionInterval;
    }
}