package com.example.iotmonitoring.exception;

/**
 * Custom exception for invalid data formats in IoT device data.
 */
public class InvalidDataFormatException extends RuntimeException {
    public InvalidDataFormatException(String message) {
        super(message);
    }
}