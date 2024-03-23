
## NOT FINISHED 
"""
class servo9g:
    def setAngle(deg):
            pulse = 1.5 + (deg * (0.5/90))
            pulse = round(pulse, 3)
            print("Pulse set to %s" % pulse)
"""


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
        print("Pin info: %s" % pinInfo)
        if isinstance(pinInfo, list):
            return int(str(pinInfo[0][len(pinInfo[0])-1])) * 32 + int(letters.index(pinInfo[1][0])) * 8 + int(pinInfo[1][1])
        
        else:
            return str(pinInfo)

    
    def initialize(pinout):
        pins.pinout = pinout
    
    
    def setPin(pin, state):
        try: 
            toggle = int(pins.parsePinout(pin, pins.pinout))
            print("toggle is %s" % toggle)

            if state < 0 or state > 1: 
                raise ValueError
            
            if isinstance(toggle, int):
                try:
                    import os
                    
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
        

              



