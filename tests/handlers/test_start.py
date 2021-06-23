from forty.actions import Action, Actions
from forty.handlers import StartHandler

from .handler_test_case import HandlerTestCase


class TestStartHangler(HandlerTestCase):
    def __init__(self, *args, **kwargs):
        HandlerTestCase.__init__(self, *args, **kwargs)

    @property
    def handler_class(self):
        return StartHandler

    def test_default(self):
        timestamp = self.tm.get_datetime()

        self.handle([])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.pm.save_actions.assert_called_once_with([Action(type=Actions.START, timestamp=timestamp)])
        self.om.emmit.assert_called_once_with("start/test_time_now")

    def test_specific_time(self):
        timestamp = self.tm.merge_time()
        
        self.handle(["12:34:56"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.pm.save_actions.assert_called_once_with([Action(type=Actions.START, timestamp=timestamp)])
        self.om.emmit.assert_called_once_with("start/test_time_merge")

    def test_do_nothing(self):
        self.actions_to_return([Action(type=Actions.START, timestamp=None)])

        self.handle([])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.om.emmit.assert_called_once_with("already started")
