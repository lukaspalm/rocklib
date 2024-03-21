
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


              



