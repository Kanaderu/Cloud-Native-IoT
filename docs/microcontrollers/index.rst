################
Microcontrollers
################

Microcontrollers are ideal for low-powered, low-cost, reliable, edge compute to perform simple tasks. Microcontrollers are typically developed in a fairly low-level language, commonly C or C++ operating at a fairly low clock-speed ranges (MHz) . Common microcontrollers include many arduino and adafruit devices that include the ESP8266, ESP32, STM32, PIC32, ATmega, ARM Cortex (M0, M3, M4, M7, M33), MCS, etc.

In comparison, Microprocessors are used for more complex tasks consuming more power, high clock speeds (GHz), less reliable, and more suitable for running more parallel tasks or even full operating systems. The most popular include common single-board computers (SBC) such as the Raspberry Pi, Orange Pi, ODroids, BeagleBone, Nvidia Jetson, Le Potato, and many smartphone devices.

------------------------------------------
AWS M5Stack ESP32 IoT Core Development Kit 
------------------------------------------

The AWS M5Stack ESP32 is the device used as an example here for developing on a microcontroller.

M5Stack Datasheet
-----------------

.. image:: /assets/microcontrollers/CORE2_V1.0_SCH_page_01.png
   :alt: AWS IoT Core 2 Schematics
   :align: center

Referneces
^^^^^^^^^^

- M5Stack Documentation https://docs.m5stack.com/ 
- ESP-IDF ESP32 Documentation https://docs.espressif.com/projects/esp-idf/en/stable/esp32/index.html
- ESP-IDF M5Stack Core 2 Component https://components.espressif.com/components/espressif/m5stack_core_2/versions/2.0.0
- ESP-IDF M5Stack BSP https://docs.m5stack.com/en/esp_idf/m5core2/bsp
- ESP-IDF Docker Documentation https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/tools/idf-docker-image.html