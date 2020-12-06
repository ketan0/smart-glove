#!/usr/bin/env python3

import os

from phue import Bridge

b = Bridge(os.environ['HUE_BRIDGE_IP'])
light_names = b.get_light_objects('name')

def turn_on_lights():
    for light in ['Mom', 'Dad']:
        light_names[light].on = True

def turn_off_lights():
    for light in ['Mom', 'Dad']:
        light_names[light].on = False

def change_light_colors():
    for light in ['Mom', 'Dad']:
        light_names[light].hue = 1000
        light_names[light].brightness = 254
        light_names[light].saturation = 254

def adjust_light_property(prop, inc=1000):
    for light in ['Mom', 'Dad']:
        b.set_light(light, prop, b.get_light(light, prop) + inc)
