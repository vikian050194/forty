import json
import subprocess


filename = "settings.json"


class Settings():
    def __init__(self, data):
        self.hours = data['hours']
        self.minutes = data['minutes']
        self.seconds = data['seconds']

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


def get_settings():
    fp = open(filename, "r")
    return json.load(fp)


def send_message(title, message):
    subprocess.Popen(['notify-send', title, message])
    return


from threading import Timer


class RepeatedTimer():
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.daemon = False
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False