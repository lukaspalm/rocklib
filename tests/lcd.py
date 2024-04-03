import time
from rocklib import pins, pinouts


class lcd:
    def initialize(pinout, RS, E, D4, D5, D6, D7):
        pins.initialize(pinout)
        lcd.dataPins = [D4, D5, D6, D7]
        lcd.RS = RS
        lcd.E = E
        fourBitMode = [["0010", "0000"]]
        clearScreen = [["1000", "0000"]]
        returnHome = [["0100", "0000"]]
        displayOn = [["0011"]]

        pins.setPin(lcd.RS, 0)
        pins.setPin(lcd.E, 0)
        pins.setPin(D4, 0)
        pins.setPin(D5, 0)
        pins.setPin(D6, 0)
        pins.setPin(D7, 0)

        lcd.sendLcd(fourBitMode)
        lcd.sendLcd(clearScreen)
        lcd.sendLcd(returnHome)
        lcd.sendLcd(displayOn)

        pins.setPin(lcd.RS, 1)




    def sendLcd(bins):
        for pair in bins:
            for part in pair:
                pins.setPin(lcd.E, 0)
                partchars = list(str(part))
                number = 0
                for char in partchars:
                    time.sleep(0.025)
                    if char == "1":
                        print("Data %s HIGH" % (number + 4))
                        pins.setPin(lcd.dataPins[number], 1)
                    if char == "0":
                        print("Data %s LOW" % (number + 4))
                        pins.setPin(lcd.dataPins[number], 0)
                    number += 1
                print("E HIGH")
                pins.setPin(lcd.E, 1)


    def write(string):
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
        
        lcd.sendLcd(parsedBins)


lcd.initialize(pinouts.ROCK4, RS=11, E=13, D4=29, D5=31, D6=33, D7=37)
lcd.write("HELLO")

