# SMART-PARKING-SYSTEM-WITH-LICENSE-PLATE-RECOGNITION
<img width="1343" height="593" alt="image" src="https://github.com/user-attachments/assets/4865ef51-669a-465a-bab9-8fcb26666ff5" />
1. Abstract
This project is a smart parking system with two parking spots. At the entrance, a USB camera is used to read the vehicle’s license plate and the barrier opens for authorized cars. Inside the parking area, the full/empty status of two parking spots is detected using IR sensors and shown with LEDs. If a spot is empty, the green LED turns ON. If it is full, the red LED turns ON.
The system has two parts:
•
Arduino: Parking occupancy detection and LED control
•
Raspberry Pi: License plate recognition with camera and barrier control using a servo motor
2. Real-Life Problem and Solution
2.1 Problem
Parking lots commonly have these problems:
•
Drivers spend time searching for an empty spot, which causes time loss and traffic.
•
Parking areas become crowded because drivers make unnecessary moves when a spot is full.
•
Manual barrier control can allow unauthorized entry and human mistakes.
•
Barrier control and guidance require continuous human work.
2.2 Solution
This project solves these problems by:
•
Showing parking spot occupancy in real time with IR sensors and LEDs (2 spots).
•
Controlling the entrance barrier automatically using license plate recognition and a servo motor.
3. System Architecture and Working Principle
3.1 Parking Occupancy System (Arduino) – 2 Spots
•
Two IR sensors are used (one sensor per parking spot).
•
The sensor output is read from Arduino digital input pins.
•
If a car is detected: FULL → Red LED ON, Green LED OFF
•
If no car is detected: EMPTY → Green LED ON, Red LED OFF
The IR sensors used in this project work as Active-Low: when a car/obstacle is detected → OUT = LOW. The Arduino code is written according to this behavior.
3.2 License Plate Recognition + Barrier (Raspberry Pi)
•
Raspberry Pi captures frames from the USB camera.
•
Plate text is extracted using plate recognition (OCR / image processing).
•
The plate is compared with an authorized list.
•
If authorized, the servo motor opens the barrier and closes it after a delay.
4. Materials Used
•
Arduino (Uno / Nano etc.)
•
Raspberry Pi 4
•
USB camera (Logitech C310)
•
2 IR sensor modules (OUT–VCC–GND)
•
1 servo motor (barrier mechanism)
•
LEDs for 2 parking spots: 2 red + 2 green
•
Jumper wires
5.1.2 IR Sensor Connections (2 sensors)
COMPONENTS
SENSOR PIN
ARDUINO PIN
DESCRIPTION
IR SENSOR 1
VCC
5V
Sensor power
IR SENSOR 1
GND
GND
Common ground
IR SENSOR 1
OUT
D2
Parking spot 1 input
IR SENSOR 2
VCC
5V
Sensor power
IR SENSOR 2
GND
GND
Common ground
IR SENSOR 2
OUT
D3
Parking spot 2 input
5.1.3 LED Connections (4 LEDs)
In this project, the LEDs were connected without series resistors.
Connection logic used: Arduino pin → LED anode (+) → LED cathode (–) → GND
LED
ARDUINO PIN
Spot 1 Red
D8
Spot 1 Green
D9
Spot 2 Red
D10
Spot 2 Green
D11
5.2 Raspberry Pi Connections (Camera + Servo)
5.2.1 Camera Connection
•
Logitech C310 camera is connected via USB.
•
Resolution is set in software to 640 × 480.
5.2.2 Servo Connection (Barrier)
SERVO WIRE
RASPBERRY PI CONNECTIONS
DESCRIPPTION
Servo VCC
5V
Servo power
Servo GND
GND
Common ground
Servo Signal
GPIO18 (BCM) / Physical Pin 12
PWM control signal
6. Software and Algorithm
6.1 Arduino Software (Parking Occupancy) – Analysis
•
Arduino reads IR1 (D2) and IR2 (D3).
•
If IR output is LOW, it means “car present”, and it turns ON red LED and turns OFF green LED.
•
If IR output is HIGH, it means “no car”, and it turns ON green LED and turns OFF red LED.
Decision table:
IR OUT
STATUS
GREEN LED
RED LED
LOW
FULL
OFF
ON
HIGH
EMPTY
ON
OFF
6.2 Raspberry Pi Software (Plate Recognition + Barrier) – Analysis
6.2.1 Camera Loop
•
The program opens the camera with cv2.VideoCapture(CAMERA_SOURCE).
•
Frame size is set to 640×480.
•
The program reads frames continuously and shows the live video window.
•
Pressing ‘q’ exits the program.
6.2.2 Plate Recognition and Authorization Logic
•
recognize_plate_from_frame(frame) returns:
o
plate (best guess),
o
confidence,
o
candidates (other guesses).
•
The program checks the candidate list first. If one candidate is in the authorized list, status becomes AUTHORIZED.
•
If no candidate matches, it checks the best guess. If it is authorized, status becomes AUTHORIZED.
•
Otherwise, status stays UNAUTHORIZED.
6.2.3 Anti-Repeat Logic
•
The program stores last_plate and last_ts.
•
If the same plate appears again within 5 seconds, it does not log again and does not trigger the servo again.
6.2.4 Event Logging
•
When a new plate event happens, the current frame is saved as an image file.
•
The event is logged with plate, confidence, status, camera ID, time, and image path.
6.2.5 Barrier Control
•
Servo runs only when a new AUTHORIZED plate event happens.
•
Sequence:
o
open_barrier()
o
wait 7.0 seconds
o
close_barrier()
6.3 System Operating Rules
•
The system works in real time. Parking LEDs change immediately based on the IR sensor outputs. On Raspberry Pi, the same plate is not processed again within 5 seconds. If a plate is AUTHORIZED, the barrier opens and closes after 7 seconds.
Estimated Cost
ITEM
QTY
UNIT PRICE(TRY)
Arduino Uno
1
187,13
Raspberry Pi 4(2GB)
1
2.758,40
USB Camera (Logitech C310)
1
849,00
IR Sensor Module
2
51,48
Servo Motor (SG90)
1
70,78
LEDs (red + green)
4
4,37
Jumper wires
1 set
46,84
Power adapter(s) / cables
1
488,19
Total (Estimated)
-
4.459,19
8. Tests and Results
•
Spot 1 and Spot 2 show green when empty and red when full.
•
When an AUTHORIZED plate is detected, the servo opens the barrier and closes it after the delay.
•
The same plate does not trigger the system again within 5 seconds.
9. Conclusion
This project combines two-spot occupancy detection (Arduino + IR sensors + LEDs) and automatic entrance control (Raspberry Pi + USB camera + plate recognition + servo barrier).




