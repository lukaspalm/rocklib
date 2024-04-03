
#------------------ Camera Testing ------------------#
"""
from rocklib import camera
camera.takePicture(out="test.jpg", device="/dev/video0")
"""


#------------------ LCD 16x2 Development ------------------#

"""
from rocklib import lcd

lcd.lcd_init() 

D0-D3 = 0

D4-D7 = inputdata


RS      Binary
0       0100 (4-bit mode, 1 line)
0       0000
0       0001 (clear screen)
0       0000
0       0010 (return home)
0       0000
0       1100 (display on, cursor off, blink off)

1       xxxx
1       xxxx (character 1)

Example: 

[!] NOTE: The LCD screen is in 4-bit mode, 1 line and it is reversed.

A       0100 0001

RS      Binary
1       0010  D4=0 D5=0 D6=1 D7=0
1       1000

E = HIGH

initialising the LCD screen and clearing the screen
https://www.youtube.com/watch?v=cXpeTxC3_A4
"""
#Parsing a string to computable binary

def sendLcd(bins):
    for pair in bins:
        for part in pair:
            partchars = list(str(part))
            number = 4
            for char in partchars:
                if char == "1":
                    print("Data %s HIGH" % number)
                if char == "0":
                    print("Data %s LOW" % number)
                number += 1
            print("E HIGH")


def parseString(string):
    chars = list(string)
    binarys = []
    parsedBins = []
    for char in chars:
        binchar = bin(ord(char))[2:]
        binchar = binchar.zfill(8)
        binarys.append(binchar)

    for binchar in binarys:
        templist = []

        templist.append(binchar[3::-1])
        templist.append(binchar[:3:-1])

        parsedBins.append(templist)
    
    sendLcd(parsedBins)



parseString("HelloWorld")


#----------------- Parse Pinout -----------------#
"""
def parsePinout(pinout, device):
    letters = "ABCD"
    pinInfo = device[pinout]
    if isinstance(pinInfo, list):
        return [str(pinInfo[0]), str(int(letters.index(pinInfo[1][0])) * 8 + int(pinInfo[1][1]))]
    
    else:
        return str(pinInfo)
"""




#----------------- Pin Control (gpiod) -----------------#





