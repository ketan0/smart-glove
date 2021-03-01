#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
from dotenv import load_dotenv
load_dotenv()
from config import *
from glove_state import GloveState
from spotify_controls import toggle_playback, add_current_song_to_playlist, next_track, prev_track
from messenger_controls import send_message, send_message_self
from hue_controls import adjust_light_property, random_light_colors, toggle_lights, turn_off_lights, turn_on_lights

def handle_key(key, state):
    active_mode = state.get_active_mode()
    if active_mode == 'select':
        desired_mode = {
            '1': 'spotify',
            '2': 'messenger',
            '3': 'hue'
        }.get(key, None)
        if desired_mode:
            state.set_active_mode(desired_mode)
        else:
            print('Invalid key. try again.')
    elif active_mode == 'spotify':
        # TODO: wrap this block in a GloveLayout class; save the instantiations as constants
        # in config.py, then just do state = GLOVE_LAYOUTS[active_mode].handle_key(key, state)
        # or perhaps state = handle_key(key, glove_layout, state) is a separate functoin
        desired_action = {
            '0': lambda: state.set_active_mode('select'),
            '1': toggle_playback,
            '2': lambda: add_current_song_to_playlist(SPOTIFY_PLAYLIST_ID), # chill playlist
            '3': prev_track,
            '4': next_track,

        }.get(key, None)
        if desired_action:
            desired_action()
        else:
            print('Invalid key. try again.')
    elif active_mode == 'messenger':
        desired_action = {
            '0': lambda: state.set_active_mode('select'),
            '1': lambda: send_message('🔴', MESSENGER_ID),
            '2': lambda: send_message('⭕', MESSENGER_ID),
            '3': lambda: send_message('💭', MESSENGER_ID),
            '4': lambda: send_message('🗣', MESSENGER_ID),
            '5': lambda: send_message('❓', MESSENGER_ID),
        }.get(key, None)
        if desired_action:
            desired_action()
        else:
            print('Invalid key. try again.')
    elif active_mode == 'hue':
        desired_action = {
            '0': lambda: state.set_active_mode('select'),
            '1': toggle_lights,
            '2': turn_off_lights,
            '3': random_light_colors,
            '4': lambda: adjust_light_property('hue', inc=5000),
            '5': lambda: adjust_light_property('hue', inc=-5000),
            '6': lambda: adjust_light_property('sat', inc=50),
            '7': lambda: adjust_light_property('sat', inc=-50),
            '8': lambda: adjust_light_property('bri', inc=50),
            '9': lambda: adjust_light_property('bri', inc=-50),
        }.get(key, None)
        if desired_action:
            desired_action()
        else:
            print('Invalid key. try again.')
    else:
        print('Mode not implemented yet. entering select mode')
        state.set_active_mode('select')

    return state

def main():
    state = GloveState()
    GPIO.setmode(GPIO.BCM)
    for channel in PINS_TO_FINGERS:
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(channel, GPIO.RISING,
                              callback=lambda channel: handle_key(PINS_TO_FINGERS[channel], state),
                              bouncetime=1000)
    print('ready for input.')
    while True:
        time.sleep(10)

if __name__ == '__main__':
    main()
