import json
import subprocess


filename = "settings.json"


class Settings():
    def __init__(self, foo):
        self.hours = foo['hours']
        self.minutes = foo['minutes']
        self.seconds = foo['seconds']


def get_settings():
    fp = open(filename, "r")
    return json.load(fp)


def send_message(title, message):
    subprocess.Popen(['notify-send', title, message])
    return