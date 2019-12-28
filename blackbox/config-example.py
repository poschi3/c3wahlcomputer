#!/usr/bin/env python3

buttons = [
    {
        'name': 'heart-eyes',
        'button': 'GPIO12', # 12
        'led': 'GPIO7', #21
        'message': ''
    },
    {
        'name': 'smiling-face',
        'button': 'GPIO024', # 24
        'led': 'GPIO23', # 23
        'message': ''
    },
    {
        'name': 'partying-face',
        'button': 'GPIO19', # 19
        'led': 'GPIO13', # 13
        'message': ''
    },
    {
        'name': 'exploding-head',
        'button': 'GPIO08',
        'led': 'GPIO25',
        'message': ''
    },
    {
        'name': 'frowning-face',
        'button': 'GPIO6', # 6
        'led': 'GPIO5', # 5
        'message': ''
    },
    {
        'name': 'sleeping-face',
        'button': 'GPIO20', #20
        'led': 'GPIO21', #21
        'message': ''
    }
]

influxdb = {
    'host': 'example.com',
    'port': 443,
    'ssl': True,
    'verify_ssl': True,
    'user': 'username',
    'password': 'password',
    'db': 'vote',
    'device': 'terminal1'
}

printer = {
    'host': '1.1.1.1',
    'port': 1234
}
