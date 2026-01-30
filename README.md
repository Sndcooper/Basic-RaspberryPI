# Raspberry Pi Python Projects

A collection of Python scripts for Raspberry Pi hardware interfacing and control projects. These scripts demonstrate GPIO control, sensor integration, socket communication, and hardware automation.

## 📋 Project List

| Script | Description |
|--------|-------------|
| **led_blink.py** | Simple LED blinking with user-defined repetitions |
| **pwm_brightness_control.py** | LED brightness control using PWM with pushbuttons |
| **pwm_basic.py** | Basic PWM signal generation example |
| **ir_brightness_arduino.py** | Control IR LED brightness using Arduino ADC via serial |
| **arduino_serial_reader.py** | Read analog values from Arduino and convert to voltage |
| **gpio_input_detector.py** | GPIO input detection with LED control |
| **pir_sensor.py** | PIR motion sensor reading |
| **pushbutton_toggle.py** | Toggle LED state with pushbutton |
| **4x4_keypad.py** | 4x4 matrix keypad input reader |
| **keypad_input_class.py** | Object-oriented keypad input handler with return character |
| **servo_arduino_control.py** | Servo motor angle control using Arduino potentiometer |
| **ultrasonic_distance.py** | HC-SR04 ultrasonic sensor distance measurement |
| **security_system.py** | Integrated security system with keypad, ultrasonic, and servo |
| **udp_socket_server.py** | UDP socket server for receiving commands |
| **udp_gpio_control.py** | GPIO control via UDP socket commands |
| **socket_basic.py** | Basic socket communication example |
| **vpython_animation.py** | VPython 3D ball animation demo |

## 🔧 Hardware Requirements

- Raspberry Pi (any model with GPIO)
- LEDs and resistors
- Pushbuttons
- 4x4 Matrix Keypad
- HC-SR04 Ultrasonic Sensor
- PIR Motion Sensor
- Servo Motor
- IR LED
- Arduino (for serial communication scripts)
- Jumper wires and breadboard

## 📦 Dependencies

```bash
sudo apt-get update
sudo apt-get install python3-rpi.gpio
pip3 install pyserial vpython
```

## 🚀 Usage

Each script can be run directly:
```bash
python3 <script_name>.py
```

Most scripts include keyboard interrupt handling (Ctrl+C) for clean GPIO cleanup.

## ⚠️ Important Notes

- Always run scripts with appropriate permissions
- Ensure correct GPIO pin connections before running
- Most scripts use BOARD pin numbering mode
- Remember to cleanup GPIO after use to prevent conflicts

## 📝 License

Free to use for educational and personal projects.

## 👤 Author

Vilas - Raspberry Pi Enthusiast
