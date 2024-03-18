# Rocklib

A universal python library for GPIO control using [Radxa](https://wiki.radxa.com/) PCBs.

>[!Warning]
> This library does not yet exist on pypi, as this is a work in progress.  
> The code may not be complete. Wait for release, or do debugging yourself.





## Features and Supported Devices

:red_circle: - Not started  
:yellow_circle: - Work in progress  
:green_circle: - Done and ready to use  

&nbsp;

### X-Series
 | Feature/Device | X2L |
 | :--- | :---: |
 | Pinouts | 🟡 |
 | 16x2 LCD Display | 🔴 |
 | Individual pin on/off | 🔴 |
 | Individual pin read input | 🔴 |
 | Servo-Motor | 🔴  |
 | Stepper-Motor | 🔴 |
 | Motion Detector | 🔴 |
 | Keypad ([link](https://m.media-amazon.com/images/I/61VWsKXQmUL._AC_UF1000,1000_QL80_.jpg)) | 🔴 |
 | Ultrasonic Sensor (HC-SR04) | 🔴 | 

&nbsp;

### E-Series
 | Feature/Device | Rock Pi E |
 | :--- | :---: |
 | Pinouts | 🟡 |
 | 16x2 LCD Display | 🔴 |
 | Individual pin on/off | 🔴 |
 | Individual pin read input | 🔴 |
 | Servo-Motor | 🔴  |
 | Stepper-Motor | 🔴 |
 | Motion Detector | 🔴 |
 | Keypad ([link](https://m.media-amazon.com/images/I/61VWsKXQmUL._AC_UF1000,1000_QL80_.jpg)) | 🔴 |
 | Ultrasonic Sensor (HC-SR04) | 🔴 | 
 
&nbsp;

### Zero-Series
 | Feature/Device | Zero | Zero 2 Pro | Zero 3E | Zero 3W |
 | :--- | :---: | :---: | :---: | :---: |
 | Pinouts | 🟡 | 🟡 | 🟡 | 🟡 | 
 | 16x2 LCD Display | 🔴 | 🔴 | 🔴 | 🔴 | 
 | Individual pin on/off | 🔴 | 🔴 | 🔴 | 🔴 |
 | Individual pin read input | 🔴 | 🔴 | 🔴 | 🔴 |
 | Servo-Motor | 🔴 | 🔴 | 🔴 | 🔴 |
 | Stepper-Motor | 🔴 | 🔴 | 🔴 | 🔴 |
 | Motion Detector | 🔴 | 🔴 | 🔴 | 🔴 |
 | Keypad ([link](https://m.media-amazon.com/images/I/61VWsKXQmUL._AC_UF1000,1000_QL80_.jpg)) | 🔴 |  🔴 | 🔴 | 🔴 |
 | Ultrasonic Sensor (HC-SR04) | 🔴 | 🔴 | 🔴 | 🔴 |

&nbsp;

### Rock S-Series
 | Feature/Device | Rock Pi S | Rock S0 |
 | :--- | :---: | :---: |
 | Pinouts | 🟡 | 🟡 | 
 | 16x2 LCD Display | 🔴 | 🔴 | 
 | Individual pin on/off | 🔴 | 🔴 | 
 | Individual pin read input | 🔴 | 🔴 | 
 | Servo-Motor | 🔴 | 🔴 | 
 | Stepper-Motor | 🔴 | 🔴 | 
 | Motion Detector | 🔴 | 🔴 | 
 | Keypad ([link](https://m.media-amazon.com/images/I/61VWsKXQmUL._AC_UF1000,1000_QL80_.jpg)) | 🔴 | 🔴 | 
 | Ultrasonic Sensor (HC-SR04) | 🔴 | 🔴 | 

&nbsp;

### Rock 3-Series
 | Feature/Device | Rock 3A | Rock 3B | Rock 3C |
 | :--- | :---: | :---: | :---: |
 | Pinouts | 🟡 | 🟡 | 🟡 |
 | Camera RPI v1.3 | 🟢 | N/A | 🟢 |
 | 16x2 LCD Display | 🔴 | 🔴 | 🔴 |
 | Individual pin on/off | 🔴 | 🔴 | 🔴 |
 | Individual pin read input | 🔴 | 🔴 | 🔴 |
 | Servo-Motor | 🔴 | 🔴 | 🔴 |
 | Stepper-Motor | 🔴 | 🔴 | 🔴 |
 | Motion Detector | 🔴 | 🔴 | 🔴 |
 | Keypad ([link](https://m.media-amazon.com/images/I/61VWsKXQmUL._AC_UF1000,1000_QL80_.jpg)) | 🔴 |  🔴 | 🔴 |
 | Ultrasonic Sensor (HC-SR04) | 🔴 | 🔴 | 🔴 |

&nbsp;
    
### Rock 4-Series

 | Feature/Device | Rock 4SE | Rock 4A | Rock 4A+ | Rock 4B | Rock 4B+ | Rock 4C+ |
 | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
 | Pinouts | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 
 | Camera RPI v1.3 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | N/A | 
 | 16x2 LCD Display | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 
 | Individual pin on/off | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 
 | Individual pin read input | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 
 | Servo-Motor | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 
 | Stepper-Motor | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 
 | Motion Detector | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 
 | Keypad ([link](https://m.media-amazon.com/images/I/61VWsKXQmUL._AC_UF1000,1000_QL80_.jpg)) | 🔴 |  🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 
 | Ultrasonic Sensor (HC-SR04) | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 

&nbsp;

### Rock 5-Series
 | Feature/Device | Rock 5A | Rock 5B |
 | :--- | :---: | :---: |
 | Pinouts | 🟡 | 🟡 | 
 | 16x2 LCD Display | 🔴 | 🔴 | 
 | Individual pin on/off | 🔴 | 🔴 | 
 | Individual pin read input | 🔴 | 🔴 | 
 | Servo-Motor | 🔴 | 🔴 | 
 | Stepper-Motor | 🔴 | 🔴 | 
 | Motion Detector | 🔴 | 🔴 | 
 | Keypad ([link](https://m.media-amazon.com/images/I/61VWsKXQmUL._AC_UF1000,1000_QL80_.jpg)) | 🔴 | 🔴 | 
 | Ultrasonic Sensor (HC-SR04) | 🔴 | 🔴 | 

&nbsp;


## Installation

You will need `python3-dev`, on Debian/Ubuntu. You can install this with:
```bash
sudo apt install python3-dev
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rocklib and gpiod, which is utilized for GPIO control. 

```bash
pip install rocklib gpiod
```

## Usage

### Camera
```python
from rocklib import camera

# Replace picture.png with your outfile name  
# Replace /dev/video0 with your video device

camera.takePicture(out="picture.jpg", device="/dev/video0")

```
More coming soon...

## Contributing

You can wish devices that I will add support for, if it does not already exist. View the list of  [supported devices](#Features-and-Supported-Devices).

Contact me by pinging me in the Radxa discord server `@lukaspalm`, or by sending me a DM on discord. 
## License

[MIT](https://choosealicense.com/licenses/mit/)
