from .base import AbstractView


class ActionView(AbstractView):
    def __init__(self, type, value, timestamp):
        self.type = type
        self.value = value
        self.timestamp = timestamp


__all__ = ["ActionView"]
