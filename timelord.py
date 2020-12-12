#!/usr/bin/env python3

from utils import *

data = get_settings()

state = Settings(data)

print(state)
print(state.hours)
print(state.minutes)
print(state.seconds)

state.hours = 0
state.minutes = 0
state.seconds = 3

def tick():
    state.seconds = state.seconds - 1
    if state.seconds == -1:
        state.seconds = 59
        state.minutes = state.minutes - 1
    
    if state.minutes == -1:
        state.minutes = 59
        state.hours = state.hours - 1

    if state.hours == -1:
        send_message('timelord', 'time is up')

    print(state)


# rt = RepeatedTimer(1, tick)

from time import sleep

def hello(name):
    print(f'Hello {name}!')

print('starting...')
rt = RepeatedTimer(1, hello, 'World') # it auto-starts, no need of rt.start()
try:
    sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!