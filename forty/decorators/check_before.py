from ..views import ErrorView
from ..models import HistoryModel


def check_before(func):
    def wrapper(self, *args, **kwargs):
        model = HistoryModel(self.pm, self.tm)
        invalid_dates = model.check_all()
        today = self.tm.get_date()
        invalid_dates = list(filter(lambda x: x != today, invalid_dates))
        if invalid_dates:
            dates = ", ".join(map(str, invalid_dates))
            return ErrorView(f"invalid state at {dates}")
        else:
            return func(self, *args, **kwargs)
    return wrapper


__all__ = ["check_before"]
