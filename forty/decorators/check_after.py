from forty.views import ErrorView
from forty.models import HistoryModel


def check_after(func):
    def wrapper(self, *args, **kwargs):
        model = HistoryModel(self.fm, self.tm)
        result = func(self, *args, **kwargs)
        invalid_dates = model.check_all()
        if invalid_dates:
            model.undo(1)
            dates = ", ".join(map(str, invalid_dates))
            return ErrorView(f"invalid state at {dates}")
        else:
            return result
    return wrapper


__all__ = ["check_after"]
