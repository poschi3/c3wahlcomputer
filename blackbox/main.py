#!/usr/bin/env python3

import config as config

from gpiozero import LED, Button, PWMLED
from time import sleep
from signal import pause
from influxdb import InfluxDBClient

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
    def __init__(self, config, store):
        self.config = config
        self.store = store

        self.button = Button(self.config['button'])
        self.button.when_pressed = self.buttonPressed
        self.led = PWMLED(self.config['led'])
#        self.led.source = self.button

    def pulse(self):
        self.led.pulse()
 
    def buttonPressed(self):
        print("Pressed: " + self.config['name'])
        self.store.vote(self.config['name'])
#        self.led.blink()
        pass # TODO REST

influx = Influx(config.influxdb)


b = []
for button in config.buttons:
    b.append(Voter(button, influx))

for but in b:
    but.pulse()

pause()

