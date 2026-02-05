package com.example.iotmonitoring.config;

import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.cache.CacheManager;
import org.springframework.cache.concurrent.ConcurrentMapCacheManager;

/**
 * Configuration class for enabling caching in the application.
 */
@Configuration
@EnableCaching
public class CacheConfig {
    /**
     * Bean for CacheManager to manage caches.
     * @return CacheManager instance.
     */
    @Bean
    public CacheManager cacheManager() {
        return new ConcurrentMapCacheManager("deviceDataCache");
    }
}