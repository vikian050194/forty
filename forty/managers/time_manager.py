import abc
from datetime import datetime, date, time, timedelta, timezone


class AbstractTimeManager(abc.ABC):
    @abc.abstractmethod
    def get_time(self) -> time:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_date(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_datetime(self) -> datetime:
        raise NotImplementedError()

    @abc.abstractmethod
    def merge_time(self, time: time) -> datetime:
        raise NotImplementedError()

    @abc.abstractmethod
    def merge_date(self, date: date) -> datetime:
        raise NotImplementedError()


class TimeManager(AbstractTimeManager):
    def __init__(self, tz_name: str = None, tz_offset: int = None):
        self.timezone = datetime.now().astimezone().tzinfo
        if tz_name and tz_offset:
            self.timezone = timezone(name=tz_name, offset=timedelta(seconds=tz_offset))

    def get_time(self) -> time:
        return self.get_datetime().time()

    def get_date(self) -> date:
        return self.get_datetime().date()

    def get_datetime(self) -> datetime:
        return datetime.now(tz=self.timezone)

    def merge_time(self, time: time) -> datetime:
        now = self.get_datetime()
        return datetime.combine(now.date(), time)

    def merge_date(self, date: date) -> datetime:
        now = self.get_datetime()
        return datetime.combine(now.date(), date)

# time_manager = TimeManager(tz_name="MSK", tz_offset=10800)
# time_manager = TimeManager()
# print(time_manager.get_datetime())
# print(time_manager.get_date())
# print(time_manager.get_time())

__all__ = ["TimeManager"]
