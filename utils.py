import json
import subprocess


filename = "state.json"


class State():
    def __init__(self, data):
        self.hours = data['hours']
        self.minutes = data['minutes']
        self.seconds = data['seconds']

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


def load_state():
    with open(filename, "r") as fr:
        return State(json.load(fr))


def save_state(state):
    data = dict(
        hours=state.hours,
        minutes=state.minutes,
        seconds=state.seconds
    )
    with open(filename, "w") as fw:
        json.dump(data, fw)


def send_message(title, message):
    subprocess.Popen(['notify-send', title, message])
    return


from threading import Event, Thread

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        while not stopped.wait(interval):
            func(*args)
    Thread(target=loop).start()    
    return stopped.set


def tick(state):
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
