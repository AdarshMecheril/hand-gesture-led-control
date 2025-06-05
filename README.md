# 🤚 Hand Gesture LED Control using OpenCV & Arduino

This project enables control of 5 LEDs using simple hand gestures captured via a webcam. Utilizing **OpenCV** and **MediaPipe**, the system detects finger gestures in real-time and communicates with an Arduino Uno to illuminate LEDs corresponding to the number of fingers raised.

---

## 📁 Project Structure

```
hand-gesture-led-control/
├── Arduino/
│   └── led_control.ino          # Arduino code to control the LEDs
├── Python/
│   └── hand_tracking_led.py     # Python code to track hand gestures and send signals
├── images/
│   └── circuit_diagram.png      # Circuit diagram image
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔌 Circuit Diagram

The following diagram illustrates the connection of 5 LEDs to the Arduino Uno:

![Circuit Diagram](images/circuit_diagram.png)

Each LED is connected to a digital pin on the Arduino, with a 220Ω resistor in series to prevent overcurrent.

| LED Number | Arduino Pin |
|------------|-------------|
| LED 1      | D2          |
| LED 2      | D3          |
| LED 3      | D4          |
| LED 4      | D5          |
| LED 5      | D6          |

Ensure all LED cathodes are connected to GND.

---

## 🛠 Requirements

- Arduino Uno R3
- 5 LEDs
- 5 × 220Ω resistors
- Breadboard and jumper wires
- USB cable
- PC or laptop with Python installed
- Webcam (built-in or external)

---

## 💡 How It Works

1. The webcam captures your hand in real-time.
2. The Python script processes the hand using MediaPipe and determines the number of fingers raised.
3. Based on the count (0 to 5), a corresponding number is sent via serial communication to the Arduino.
4. The Arduino receives the number and activates that many LEDs starting from pin D2.

**Example**:
- Raising 3 fingers → LEDs on D2, D3, and D4 turn ON.
- Making a fist (0 fingers) → All LEDs turn OFF.

---

## 🧪 Getting Started

### Step 1: Install Python Dependencies

```bash
pip install opencv-python mediapipe pyserial
```

### Step 2: Run the Python Script

Navigate to the `Python` directory and execute the script. Ensure the serial port (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux) matches your Arduino's connection.

```bash
python hand_tracking_led.py
```

### Step 3: Upload Arduino Code

Use the Arduino IDE to upload `led_control.ino` from the `Arduino` directory to your Arduino Uno.

---

## 🚀 Possible Extensions

- Implement more complex gestures to control different devices.
- Replace LEDs with relays to manage higher voltage appliances.
- Develop a comprehensive hand-controlled interface for IoT or robotics applications.

---

## 👨‍💻 Author

**Adarsh Mecheril**

Feel free to fork the project, suggest improvements, or contribute!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---











