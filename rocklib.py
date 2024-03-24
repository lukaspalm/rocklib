import os

class camera:
    
    def takePicture(out, device="/dev/video0"):
        import os
        if os.path.exists(device):

            print("Taking picture and saving to %s" % out)
            try:
                os.system(f"gst-launch-1.0 v4l2src \"{device}\" io-mode=4 videoconvert video/x-raw,format=UYVY,width=1920,height=1080 jpegenc multifilesink \"location={out}\"  > /dev/null 2>&1 | timeout 3", )
                print("Picture saved to %s sucessfully!" % out)
                
            except Exception as e:
                print("Error: %s" % e)

        else:
            print("\nError: %s could not be found. \nMake sure the camera overlay is enabled and the camera is connected." % device)

class pins:
    def parsePinout(pin, mapping):
        letters = "ABCD"
        pinInfo = mapping[pin]
        if isinstance(pinInfo, list):
            return int(str(pinInfo[0][len(pinInfo[0])-1])) * 32 + int(letters.index(pinInfo[1][0])) * 8 + int(pinInfo[1][1])
        
        else:
            return str(pinInfo)

    
    def initialize(pinout):
        pins.pinout = pinout
    
    
    def setPin(pin, state):
        try: 
            toggle = int(pins.parsePinout(pin, pins.pinout))

            if state < 0 or state > 1: 
                raise ValueError
            
            if isinstance(toggle, int):
                try:
                    import os
                    
                    if os.path.exists(f"/sys/class/gpio/gpio{toggle}"):
                        with open(f"/sys/class/gpio/gpio{toggle}/direction", "w") as f:
                            f.write("out")
                            f.close()
                        with open(f"/sys/class/gpio/gpio{toggle}/value", "w") as f:
                            f.write(str(state))
                            f.close()
                    
                    else:
                        with open("/sys/class/gpio/export", "w") as f:
                            f.write(str(toggle))
                            f.close()
                        with open(f"/sys/class/gpio/gpio{toggle}/direction", "w") as f:
                            f.write("out")
                            f.close()
                        with open(f"/sys/class/gpio/gpio{toggle}/value", "w") as f:
                            f.write(str(state))
                            f.close()

                except Exception as e:
                    print("Error: %s" % e)
            else: 
                print("Error: %s not possible to toggle" % pins.pinout[pin])
        except ValueError:
            print("Error toggling pin %s.\nMake sure that the pin is not GND, 5V or 3.3v.\nAlso, make sure that the toggle value is 0 or 1." % pin)

    def getPin(pin):
        

        try:
            toggle = int(pins.parsePinout(pin, pins.pinout))
            if os.path.exists(f"/sys/class/gpio/gpio{toggle}"):

                with open(f"/sys/class/gpio/gpio{toggle}/direction", "w") as f:
                    f.write("in")
                    f.close()

                with open(f"/sys/class/gpio/gpio{toggle}/value", "r") as f:
                    value = f.read()
                    f.close()
                    return value
            else:

                with open("/sys/class/gpio/export", "w") as f:
                    f.write(str(toggle))
                    f.close()
                
                with open(f"/sys/class/gpio/gpio{toggle}/direction", "w") as f:
                    f.write("in")
                    f.close()
                
                with open(f"/sys/class/gpio/gpio{toggle}/value", "r") as f:
                    value = f.read()
                    f.close()
                    return value
        
        except Exception as e:
            print("Error: %s" % e)
            return None
        


class pinouts:
    def __init__(self):
        self.ROCK4 = {
            1: "3.3V",
            2: "5V",
            3: ["gpiochip2", "A7"],
            4: "5V",
            5: ["gpiochip2", "B0"],
            6: "GND",
            7: ["gpiochip2", "B3"],
            8: ["gpiochip4", "C4"],
            9: "GND",
            10: ["gpiochip4", "C3"],
            11: ["gpiochip4", "C2"],
            12: ["gpiochip4", "A3"],
            13: ["gpiochip4", "C6"],
            14: "GND",
            15: ["gpiochip4", "C5"],
            16: ["gpiochip4", "D2"],
            17: "3.3V",
            18: ["gpiochip4", "D4"],
            19: ["gpiochip1", "B0"],
            20: "GND",
            21: ["gpiochip1", "A7"],
            22: ["gpiochip4", "D5"],
            23: ["gpiochip1", "B1"],
            24: ["gpiochip1", "B2"],
            25: "GND",
            26: "NONE",
            27: ["gpiochip2", "A0"],
            28: ["gpiochip2", "A1"],
            29: ["gpiochip2", "B2"],
            30: "GND",
            31: ["gpiochip2", "B1"],
            32: ["gpiochip3", "C0"],
            33: ["gpiochip2", "B4"],
            34: "GND",
            35: ["gpiochip4", "A5"],
            36: ["gpiochip4", "A4"],
            37: ["gpiochip4", "D6"],
            38: ["gpiochip4", "A6"],
            39: "GND",
            40: ["gpiochip4", "A7"]
        }

pinouts = pinouts()