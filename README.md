# SMART-PARKING-SYSTEM-WITH-LICENSE-PLATE-RECOGNITION
<img width="1343" height="593" alt="image" src="https://github.com/user-attachments/assets/4865ef51-669a-465a-bab9-8fcb26666ff5" />
# SMART PARKING SYSTEM WITH LICENSE PLATE RECOGNITION

## 👥 Developers
* [cite_start]**Erhan Özgür Uzun** - 220103018 [cite: 9, 10]
* [cite_start]**Bengi Can Bengül** - 220103034 [cite: 11, 12]
* [cite_start]**Institution:** Adana Alparslan Türkeş Science and Technology University (ATU) [cite: 1, 4]

## 1. Abstract & Project Overview
[cite_start]This project is a smart parking system with two parking spots[cite: 17]. [cite_start]At the entrance, a USB camera is used to read the vehicle's license plate and the barrier opens for authorized cars[cite: 18]. [cite_start]Inside the parking area, the full/empty status of two parking spots is detected using IR sensors and shown with LEDs[cite: 19]. [cite_start]If a spot is empty, the green LED turns ON[cite: 20]. [cite_start]If it is full, the red LED turns ON[cite: 20].

## 2. Real-Life Problem and Solution
* [cite_start]**Problem:** Drivers spend time searching for an empty spot, which causes time loss and traffic[cite: 27]. [cite_start]Manual barrier control can allow unauthorized entry and human mistakes[cite: 29].
* [cite_start]**Solution:** This project solves these problems by showing parking spot occupancy in real time with IR sensors and LEDs (2 spots)[cite: 32]. [cite_start]It also controls the entrance barrier automatically using license plate recognition and a servo motor[cite: 33].

## 3. Materials Used
* [cite_start]Arduino (Uno / Nano etc.) [cite: 46]
* [cite_start]Raspberry Pi 4 (2GB) [cite: 47, 334]
* [cite_start]USB camera (Logitech C310) [cite: 48, 74]
* [cite_start]2 IR sensor modules (OUT-VCC-GND) [cite: 49]
* [cite_start]1 servo motor (SG90) (barrier mechanism) [cite: 50, 334]
* [cite_start]LEDs for 2 parking spots: 2 red + 2 green [cite: 51]
* [cite_start]Jumper wires [cite: 52]

## 4. Hardware Connections

### IR Sensor Connections
| COMPONENTS | SENSOR PIN | ARDUINO PIN | DESCRIPTION |
| :--- | :--- | :--- | :--- |
| **IR SENSOR 1** | VCC | 5V | [cite_start]Sensor power [cite: 66] |
| **IR SENSOR 1** | GND | GND | [cite_start]Common ground [cite: 66] |
| **IR SENSOR 1** | OUT | D2 | [cite_start]Parking spot 1 input [cite: 66] |
| **IR SENSOR 2** | VCC | 5V | [cite_start]Sensor power [cite: 66] |
| **IR SENSOR 2** | GND | GND | [cite_start]Common ground [cite: 66] |
| **IR SENSOR 2** | OUT | D3 | [cite_start]Parking spot 2 input [cite: 66] |

### LED Connections
| LED | ARDUINO PIN |
| :--- | :--- |
| **Spot 1 Red** | [cite_start]D8 [cite: 71] |
| **Spot 1 Green** | [cite_start]D9 [cite: 71] |
| **Spot 2 Red** | [cite_start]D10 [cite: 71] |
| **Spot 2 Green** | [cite_start]D11 [cite: 71] |

### Raspberry Pi Connections (Camera + Servo)
[cite_start]Logitech C310 camera is connected via USB[cite: 74].

| SERVO WIRE | RASPBERRY PI CONNECTIONS | DESCRIPTION |
| :--- | :--- | :--- |
| **Servo VCC** | 5V | [cite_start]Servo power [cite: 77] |
| **Servo GND** | GND | [cite_start]Common ground [cite: 77] |
| **Servo Signal**| GPIO18 (BCM) / Physical Pin 12 | [cite_start]PWM control signal [cite: 77] |

## 5. System Architecture and Working Principle
* [cite_start]**Arduino:** Two IR sensors are used (one sensor per parking spot)[cite: 36]. [cite_start]If a car is detected (LOW): Red LED ON, Green LED OFF[cite: 81, 84]. [cite_start]If no car is detected (HIGH): Green LED ON, Red LED OFF[cite: 82, 84].
* [cite_start]**Raspberry Pi:** Captures frames from the USB camera[cite: 42]. [cite_start]Plate text is extracted using plate recognition and compared with an authorized list[cite: 43]. [cite_start]If authorized, the servo motor opens the barrier and closes it after a delay[cite: 44].
* [cite_start]**Anti-Repeat Logic:** The same plate does not trigger the system again within 5 seconds[cite: 112, 338].

## 6. Estimated Cost
| ITEM | QTY | UNIT PRICE(TRY) |
| :--- | :--- | :--- |
| **Arduino Uno** | 1 | [cite_start]187.13 [cite: 334] |
| **Raspberry Pi 4(2GB)** | 1 | [cite_start]2.758.40 [cite: 334] |
| **USB Camera (Logitech C310)** | 1 | [cite_start]849,00 [cite: 334] |
| **IR Sensor Module** | 2 | [cite_start]51.48 [cite: 334] |
| **Servo Motor (SG90)** | 1 | [cite_start]70.78 [cite: 334] |
| **LEDs (red + green)** | 4 | [cite_start]4,37 [cite: 334] |
| **Jumper wires** | 1 set | [cite_start]46.84 [cite: 334] |
| **Power adapter(s) / cables** | 1 | [cite_start]488,19 [cite: 334] |
| **Total (Estimated)** | | [cite_start]**4.459,19** [cite: 334] |
