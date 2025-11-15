#####
ESP32
#####

The ESP32 is microcontroller developed by Espressif packed with many features including built-in wireless communication (wifi/bluetooth). Several variants of the chip have been made to support a variety of usecases for low-cost and low-power applications.

------------------------------------------
AWS M5Stack ESP32 IoT Core Development Kit 
------------------------------------------

The AWS M5Stack ESP32 is the device used as an example here for developing on a microcontroller.

M5Stack Datasheet
-----------------

.. image:: assets/m5stack/CORE2_V1.0_SCH_page_01.png
   :alt: AWS IoT Core 2 Schematics
   :align: center

----------------------------------------
Building and Flashing the ESP32 with IDF
----------------------------------------

Espressif uses their ESP-IDF tool to configure, build, and flash code onto their devices. For ease of use and convenience, the IDF provides a python script, ``idf.py``, to wrap around the main tools of ``CMake``, ``Ninja``, and ``esptool.py`` to build, deploy, and debug a project for the ESP32. The docker image provides a preinstalled version of the IDF tool suite to quickly begin developing a project.

Compiling a Hello World
-----------------------

To quick get started with the ESP tools, a Docker image is pulled using the command below. Containerizing the development tools enables ease of portability from having to maintain a suite of tools installed natively on the machine.

.. code-block:: bash
   :caption: Run the docker image of ESP-IDF tools

   docker run --rm -it -u root:root --dev /dev/ttyUSB0:/dev/ttyUSB0 espressif/idf:v5.5

Mount a volume for persistent data to include the hello_world example which has the following directory structure for the project root.

.. code-block:: text
   :caption: ``hello_world`` project tree

   .
   ├── CMakeLists.txt
   └── main
       ├── CMakeLists.txt
       └── hello_world_main.c

The commands below are used to

1. Set the target ESP32 device
2. Modify any additional configurations (optional)
3. Build the project
4. Flash the project to the device

References
^^^^^^^^^^

- M5Stack Documentation https://docs.m5stack.com/ 
- ESP-IDF ESP32 Documentation https://docs.espressif.com/projects/esp-idf/en/stable/esp32/index.html
- ESP-IDF M5Stack Core 2 Component https://components.espressif.com/components/espressif/m5stack_core_2/versions/2.0.0
- ESP-IDF M5Stack BSP https://docs.m5stack.com/en/esp_idf/m5core2/bsp
- ESP-IDF Docker Documentation https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/tools/idf-docker-image.html

- https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-py.html