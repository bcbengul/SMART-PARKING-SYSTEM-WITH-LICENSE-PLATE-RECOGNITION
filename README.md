# SMART-PARKING-SYSTEM-WITH-LICENSE-PLATE-RECOGNITION
<img width="1343" height="593" alt="image" src="https://github.com/user-attachments/assets/4865ef51-669a-465a-bab9-8fcb26666ff5" />
## 👥 Developers
* **Erhan Özgür Uzun** - 
* **Bengi Can Bengül** - 
* **Institution:** Adana Alparslan Türkeş Science and Technology University (ATU) - Electrical Electronics Engineering

## 1. Abstract & Project Overview
This project is a smart parking system with two parking spots. At the entrance, a USB camera is used to read the vehicle's license plate and the barrier opens for authorized cars. Inside the parking area, the full/empty status of two parking spots is detected using IR sensors and shown with LEDs. If a spot is empty, the green LED turns ON. If it is full, the red LED turns ON.

## 2. Real-Life Problem and Solution
* **Problem:** Drivers spend time searching for an empty spot, which causes time loss and traffic. Manual barrier control can allow unauthorized entry and human mistakes.
* **Solution:** This project solves these problems by showing parking spot occupancy in real time with IR sensors and LEDs (2 spots). It also controls the entrance barrier automatically using license plate recognition and a servo motor.

## 3. Materials Used
* Arduino (Uno / Nano etc.)
* Raspberry Pi 4 (2GB)
* USB camera (Logitech C310)
* 2 IR sensor modules (OUT-VCC-GND)
* 1 servo motor (SG90) (barrier mechanism)
* LEDs for 2 parking spots: 2 red + 2 green
* Jumper wires

## 4. Hardware Connections

### IR Sensor Connections
| COMPONENTS | SENSOR PIN | ARDUINO PIN | DESCRIPTION |
| :--- | :--- | :--- | :--- |
| **IR SENSOR 1** | VCC | 5V | Sensor power |
| **IR SENSOR 1** | GND | GND | Common ground |
| **IR SENSOR 1** | OUT | D2 | Parking spot 1 input |
| **IR SENSOR 2** | VCC | 5V | Sensor power |
| **IR SENSOR 2** | GND | GND | Common ground |
| **IR SENSOR 2** | OUT | D3 | Parking spot 2 input |

### LED Connections
| LED | ARDUINO PIN |
| :--- | :--- |
| **Spot 1 Red** | D8 |
| **Spot 1 Green** | D9 |
| **Spot 2 Red** | D10 |
| **Spot 2 Green** | D11 |

### Raspberry Pi Connections (Camera + Servo)
Logitech C310 camera is connected via USB.

| SERVO WIRE | RASPBERRY PI CONNECTIONS | DESCRIPTION |
| :--- | :--- | :--- |
| **Servo VCC** | 5V | Servo power |
| **Servo GND** | GND | Common ground |
| **Servo Signal**| GPIO18 (BCM) / Physical Pin 12 | PWM control signal |

## 5. System Architecture and Working Principle
* **Arduino:** Two IR sensors are used (one sensor per parking spot). If a car is detected (LOW): Red LED ON, Green LED OFF. If no car is detected (HIGH): Green LED ON, Red LED OFF.
* **Raspberry Pi:** Captures frames from the USB camera. Plate text is extracted using plate recognition and compared with an authorized list. If authorized, the servo motor opens the barrier and closes it after a delay.
* **Anti-Repeat Logic:** The same plate does not trigger the system again within 5 seconds.

## 6. Estimated Cost
| ITEM | QTY | UNIT PRICE(TRY) |
| :--- | :--- | :--- |
| **Arduino Uno** | 1 | 187.13 |
| **Raspberry Pi 4(2GB)** | 1 | 2.758.40 |
| **USB Camera (Logitech C310)** | 1 | 849.00 |
| **IR Sensor Module** | 2 | 51.48 |
| **Servo Motor (SG90)** | 1 | 70.78 |
| **LEDs (red + green)** | 4 | 4.37 |
| **Jumper wires** | 1 set | 46.84 |
| **Power adapter(s) / cables** | 1 | 488.19 |
| **Total (Estimated)** | | **4,459.19** ||
