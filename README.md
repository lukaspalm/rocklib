# Rocklib

A universal python library for GPIO control using [Radxa](https://wiki.radxa.com/) PCBs.

>[!Warning]
> This library does not yet exist on pypi, as this is a work in progress.





## Features

:red_circle: - Not started  
:yellow_circle: - Work in progress  
:green_circle: - Done and ready to use  


:green_circle: Camera (Rock Pi 4 SE)  
:yellow_circle: 16x2 LCD Display 
:yellow_circle: Individual pin on/off  
:yellow_circle: tIndividual pin read input  
:red_circle: Servo-Motor  
:red_circle: Stepper-Motor  
:red_circle: Motion Detector


## Supported Devices

- Rock Pi 4 SE  

Supported devices will be many more.  
(Rock Pi 4 SE is the only one I have for testing)


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

You can wish devices that I will add support for, if it does not already exist. View the list of  [supported devices](#Supported-Devices).

Contact me by pinging me in the Radxa discord server `@lukaspalm`, or by sending me a DM on discord. 
## License

[MIT](https://choosealicense.com/licenses/mit/)
