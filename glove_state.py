#!/usr/bin/env python3

class GloveState():
    def __init__(self):
        self.active_mode = 'select'
    def set_active_mode(self, mode):
        print(f'{mode} mode now active')
        self.active_mode = mode
    def get_active_mode(self):
        return self.active_mode
