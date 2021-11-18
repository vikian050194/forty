from typing import Optional

from datetime import time, timedelta

from .base import AbstractView
from ..actions import Actions


class TodayStatusView(AbstractView):
    def __init__(self, passed: time, remained: time):
        self.passed = passed
        self.remained = remained


class TotalStatusView(AbstractView):
    def __init__(self, passed: timedelta, remained: timedelta):
        self.passed = passed
        self.remained = remained


class PassedStatusView(AbstractView):
    def __init__(self, today: timedelta, total: timedelta):
        self.today = today
        self.total = total


class RemainedStatusView(AbstractView):
    def __init__(self, today: timedelta, total: timedelta):
        self.today = today
        self.total = total


class IntervalStatusView(AbstractView):
    def __init__(self, from_time: time, till_time: time):
        self.from_time = from_time
        self.till_time = till_time


class OnlyStatusView(AbstractView):
    def __init__(self, status: Optional[Actions]):
        self.status = status


class StatusView(AbstractView):
    def __init__(self):
        self.status: Actions = None
        self.today_passed_time: timedelta = None
        self.today_remained_time: timedelta = None
        self.total_passed_time: timedelta = None
        self.total_remained_time: timedelta = None
        self.from_time: time = None
        self.to_time: time = None


__all__ = [
    "TodayStatusView",
    "TotalStatusView",
    "PassedStatusView",
    "RemainedStatusView",
    "IntervalStatusView",
    "OnlyStatusView",
    "StatusView"
]
