#!/usr/bin/env python3

import config as config

from gpiozero import LED, Button, PWMLED
from time import sleep
from signal import pause
from influxdb import InfluxDBClient
import time
import random

class Influx:
    def __init__(self, config):
        self.config = config
        self.client = InfluxDBClient(
            host = self.config['host'],
            port = self.config['port'],
            username = self.config['user'],
            password = self.config['password'],
            database = self.config['db'],
            ssl = self.config['ssl'],
            verify_ssl = self.config['verify_ssl']
            )

    def vote(self, voting):
        data = [{
            "measurement": "vote",
            "tags": {
                "type": voting,
                "device": self.config['device']
            },
            #"time": "2009-11-10T23:00:00Z",
            "fields": {
                "value": 1
            }
        }]

        self.client.write_points(data)


class Voter:
    def __init__(self, config, orga):
        self.config = config
        self.orga = orga

        self.button = Button(self.config['button'])
        self.button.when_pressed = self.buttonPressed
        self.led = PWMLED(self.config['led'])

    def buttonPressed(self):
        print("Pressed: " + self.config['name'])
        self.orga.vote(self)


class Orga:
    def __init__(self):
        self.influx = Influx(config.influxdb)

        self.buttons = []
        for button in config.buttons:
            self.buttons.append(Voter(button, self))

    def pulse(self):
        shuffeldButtons = self.buttons.copy()
        random.shuffle(shuffeldButtons)
        for button in shuffeldButtons:
            time.sleep(0.2)
            button.led.pulse()

    def vote(self, actButton):
        otherButtons = self.buttons.copy()
        otherButtons.remove(actButton)
        actButton.led.on()
        for button in otherButtons:
            button.led.off()

        self.influx.vote(actButton.config['name'])

        time.sleep(1)
        self.pulse()




orga = Orga()
orga.pulse()

pause()

