#!/usr/bin/env python3

import config as config

from gpiozero import LED, Button, PWMLED
from time import sleep
from signal import pause

class Voter:
    def __init__(self, config):
        self.config = config
        print(self.config)

        self.button = Button(self.config['button'])
        self.button.when_pressed = self.buttonPressed
        self.led = PWMLED(self.config['led'])
#        self.led.source = self.button

    def pulse(self):
        self.led.pulse()
 
    def buttonPressed(self):
        print("Pressed" + self.config['name'])
#        self.led.blink()
        pass # TODO REST


b = []
for button in config.buttons:
    b.append(Voter(button))

for but in b:
    but.pulse()

pause()

# red = LED("GPIO18")

# button = Button("GPIO23")

# while True:
#     if button.is_pressed:
#         red.on()
#     else:
#         red.off()
