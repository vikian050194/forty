from datetime import datetime
from forty.actions import Action, WorkOptions


class DoneBuilder():
    def __init__(self, actions = [], action = None, timestamp = None):
        self.actions = actions
        self.action = action
        self.timestamp = timestamp

    def done(self):
        if self.action:
            return [*self.actions, Action(type=self.action, timestamp=self.timestamp)]
        return self.actions


class AtBuilder(DoneBuilder):
    def at(self, year=2021, month=1, day=1, hour=0, minute=0, second=0):
        actions = self.actions
        timestamp = datetime(year, month, day, hour, minute, second)
        actions = [*actions, Action(type=self.action, timestamp=timestamp)]
        return ActionsBuilder(actions, None, None)


class TestBuilder(AtBuilder):
    def test(self):
        actions = self.actions
        if self.action:
            actions = [*actions, Action(type=self.action, timestamp=self.timestamp)]
        return ActionsBuilder(actions, "test", None)


class StartBuilder(AtBuilder):
    def start(self):
        actions = self.actions
        if self.action:
            actions = [*actions, Action(type=self.action, timestamp=self.timestamp)]
        return ActionsBuilder(actions, WorkOptions.START, None)


class FinishBuilder(AtBuilder):
    def finish(self):
        actions = self.actions
        if self.action:
            actions = [*actions, Action(type=self.action, timestamp=self.timestamp)]
        return ActionsBuilder(actions, WorkOptions.FINISH, None)


class ActionsBuilder(TestBuilder, StartBuilder, FinishBuilder):
    pass
