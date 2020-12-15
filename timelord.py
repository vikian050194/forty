#!/usr/bin/env python3

from operator import add, sub
from utils import *

state = load_state()

print(state)

key = None
stop_the_world = None
restart = lambda: call_repeatedly(1, tick, state)
stop_the_world = restart()

while key != 'q':
    key = input()
    
    if key == 'q':
        stop_the_world()
        save_state(state)
        continue

    if key == 'p':
        print('pause')
        stop_the_world()
        save_state(state)
        continue
    
    if key == 'c':
        print('continue')
        stop_the_world = restart()
        continue
    
    op_key = key[:1]

    if op_key in ['+', '-']:
        op = add if op_key == '+' else sub
        data = key[1:].split(':')
        delta_h = 0
        delta_m = 0
        delta_s = 0

        if len(data) > 0 and len(data[0]):
            delta_h = int(data[0])
        if len(data) > 1 and len(data[1]):
            delta_m = int(data[1])
        if len(data) > 2 and len(data[2]):
            delta_s = int(data[2])
        
        state.hours = op(state.hours, delta_h)
        state.minutes = op(state.minutes, delta_m)
        state.seconds = op(state.seconds, delta_s)
        save_state(state)
        print(state)
        continue
