from datetime import datetime

from forty.views import ActionView, InfoView
from forty.actions import Action, WorkOptions
from forty.controllers import WorkController

from ..controller_test_case import ControllerTestCase


class TestWorkControllerStartCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return WorkController

    def test_default(self):
        timestamp = self.tm.get_datetime()

        view: ActionView = self.handle(["start"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.pm.save_actions.assert_called_once_with([Action(type=WorkOptions.START, timestamp=timestamp)])
        self.assertEqual(view.type, WorkOptions.START)
        self.assertEqual(view.timestamp, timestamp)

    def test_specific_time(self):
        self.now_to_return()
        expected = Action(type=WorkOptions.START, timestamp=datetime(2021, 1, 1, 12, 34, 56))
        
        view: ActionView = self.handle(["start", "12:34:56"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.pm.save_actions.assert_called_once_with([expected])
        self.assertEqual(view.type, WorkOptions.START)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 12, 34, 56))

    def test_do_nothing(self):
        self.actions_to_return([Action(type=WorkOptions.START, timestamp=None)])

        view: InfoView = self.handle(["start"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "already started")
