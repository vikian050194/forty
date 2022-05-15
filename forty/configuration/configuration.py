class Configuration():
    def __init__(self):
        self._home: str = None
        self._output: str = None
        self._status: str = None

    @property
    def home(self):
        return self._home

    @property
    def output(self):
        return self._output
    
    @property
    def status(self):
        return self._status
