rock4 = {}
rock4.pins = {
    1:"3.3V",
    2:"5V",
    2: ["gpiochip0", ]
}




#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

#
# This file is part of libgpiod.
#
# Copyright (C) 2017-2018 Bartosz Golaszewski <bartekgola@gmail.com>
#

'''Simplified reimplementation of the gpioget tool in Python.'''

import time

from gpiod import line

LINE = 5

with gpiod.request_lines(
    "/dev/gpiochip0",
    consumer="blink-example",
    config={
        LINE: gpiod.LineSettings(
            direction=line.Direction.OUTPUT, output_value=line.Value.ACTIVE
        )
    },
) as request:
    while True:
        request.set_value(LINE, line.Value.ACTIVE)
        time.sleep(1)
        request.set_value(LINE, line.Value.INACTIVE)
        time.sleep(1)

 