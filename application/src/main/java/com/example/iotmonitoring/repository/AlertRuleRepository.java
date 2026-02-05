package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.AlertRule;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.UUID;

/**
 * Repository interface for managing alert rules in the database.
 */
public interface AlertRuleRepository extends JpaRepository<AlertRule, UUID> {
    List<AlertRule> findByDeviceId(UUID deviceId);
}