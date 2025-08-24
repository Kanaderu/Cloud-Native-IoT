#include <stdio.h>

#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <esp_log.h>

// #include "lv_demos.h"
#include <bsp/esp-bsp.h>


static char *TAG = "app_main";

void app_main(void) {
    /* Initialize display and LVGL */
    bsp_display_start();
    /* Set display brightness to 100% */
    bsp_display_backlight_on();

    ESP_LOGI(TAG, "Hello World");

    ESP_LOGI(TAG, "Display LVGL demo");

    bsp_display_lock(0);
    bsp_display_unlock();
}
