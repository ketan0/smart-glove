#!/usr/bin/env python3

import os
import random

from phue import Bridge

b = Bridge(os.environ['HUE_BRIDGE_IP'])
light_names = b.get_light_objects('name')

def toggle_lights():
    for light in light_names:
        light_names[light].on = not light_names[light].on

def turn_on_lights():
    for light in light_names:
        light_names[light].on = True

def turn_off_lights():
    for light in light_names:
        light_names[light].on = False

def random_light_colors():
    hue, bri, sat = random.randint(0, 65535), random.randint(0, 255), random.randint(0, 255)
    for light in light_names:
        light_names[light].hue = hue
        light_names[light].brightness = bri
        light_names[light].saturation = sat

def adjust_light_property(prop, inc=1000):
    for light in light_names:
        b.set_light(light, prop, b.get_light(light, prop) + inc)
