package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.DeviceData;
import com.example.iotmonitoring.service.DataQueryService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import java.util.List;
import java.util.UUID;

import static org.mockito.Mockito.when;

/**
 * Unit tests for DataQueryController.
 */
public class DataQueryControllerTest {

    @InjectMocks
    private DataQueryController dataQueryController;

    @Mock
    private DataQueryService dataQueryService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test retrieving device data.
     */
    @Test
    public void testGetDeviceData() {
        UUID deviceId = UUID.randomUUID();
        List<DeviceData> deviceDataList = List.of(new DeviceData());
        when(dataQueryService.getDeviceData(deviceId)).thenReturn(deviceDataList);
        ResponseEntity<List<DeviceData>> response = dataQueryController.getDeviceData(deviceId);
        assert response.getStatusCode().is2xxSuccessful();
    }
}
