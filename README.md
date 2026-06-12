# Wireless Hemoglobin & Oxygen Monitoring System

## Overview
This project is an IoT-enabled healthcare device designed for continuous, remote monitoring of patient vitals. It estimates and tracks Blood Oxygen Saturation (SpO₂), Heart Rate, and Hemoglobin levels in real-time. By connecting a MAX30105/MAX30102 sensor to an ESP32/ESP8266 microcontroller, the device wirelessly transmits health data to a central Python-based dashboard for easy visualization and remote tracking.

## System Architecture
The system consists of two main components:
1. **IoT Sensor Node (Hardware):** Captures optical readings via the MAX sensor, calculates the vitals using specialized algorithms, and sends JSON payloads over Wi-Fi to the server.
2. **Real-time Dashboard (Software):** A web server receiving the HTTP POST data from the IoT node, providing a live and visually appealing user interface to display the vitals.

## File Structure
- `firmware/sensor_node.ino`: Arduino C++ code for the ESP32/ESP8266 microcontroller to read from the MAX sensor, process data, and transmit it to the dashboard.
- `dashboard/app.py`: The Python Flask backend that acts as the server to ingest sensor data and serve the web interface.
- `dashboard/templates/index.html`: The HTML/CSS/JS frontend dashboard that continuously polls the server for the latest vitals.
- `requirements.txt`: Python package dependencies required to run the dashboard.

## Setup Instructions

### 1. Hardware Setup (IoT Node)
1. Open the `firmware/sensor_node.ino` file in the Arduino IDE.
2. Update the `YOUR_WIFI_SSID` and `YOUR_WIFI_PASSWORD` variables to match your local network.
3. Update the `serverUrl` variable with the IP address of the computer running the dashboard (e.g., `http://192.168.1.100:5000/api/data`).
4. Connect your MAX30105/MAX30102 sensor to the microcontroller's I2C pins.
5. Compile and upload the code to your ESP32 or ESP8266 board.

### 2. Software Setup (Dashboard)
1. Ensure Python 3.x is installed on your machine.
2. Open a terminal or command prompt in the root directory of this project.
3. Install the necessary Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the dashboard backend server:
   ```bash
   python dashboard/app.py
   ```
5. Open your web browser and navigate to `http://localhost:5000` (or your machine's IP address on port 5000) to view the dashboard in real-time.

## Features
- **Remote Data Transmission:** Sends health vitals instantly using HTTP REST APIs.
- **Continuous Tracking:** The dashboard automatically updates every second to display the latest patient data.
- **Low-Cost Diagnostic:** Designed specifically to be accessible and cost-effective using standard, affordable microcontrollers and sensors.