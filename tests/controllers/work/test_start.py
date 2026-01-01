from datetime import datetime

from forty.views import ActionView, InfoView
from forty.actions import Action, WorkOptions
from forty.controllers.start import StartController

from ..controller_test_case import ControllerTestCase


class TestStartController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StartController

    def test_default(self):
        timestamp = self.tm.get_datetime()

        view: ActionView = self.handle([])

        self.assertEqual(self.fm.load_project.call_count, 2)
        self.assertEqual(self.fm.load_actions.call_count, 2)

        self.fm.save_actions.assert_called_once_with([Action(type=WorkOptions.START, timestamp=timestamp)])
        self.assertEqual(view.type, WorkOptions.START)
        self.assertEqual(view.timestamp, timestamp)

    def test_specific_time(self):
        self.now_to_return()
        expected = Action(type=WorkOptions.START, timestamp=datetime(2021, 1, 1, 12, 34, 56))
        
        view: ActionView = self.handle(["12:34:56"])

        self.assertEqual(self.fm.load_project.call_count, 2)
        self.assertEqual(self.fm.load_actions.call_count, 2)

        self.fm.save_actions.assert_called_once_with([expected])
        self.assertEqual(view.type, WorkOptions.START)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 12, 34, 56))

    def test_specific_date_and_time(self):
        expected = Action(type=WorkOptions.START, timestamp=datetime(2022, 6, 2, 12, 34, 56))
        
        view: ActionView = self.handle(["2022-06-02", "12:34:56"])

        self.assertEqual(self.fm.load_project.call_count, 2)
        self.assertEqual(self.fm.load_actions.call_count, 2)

        self.fm.save_actions.assert_called_once_with([expected])
        self.assertEqual(view.type, WorkOptions.START)
        self.assertEqual(view.timestamp, datetime(2022, 6, 2, 12, 34, 56))

    def test_do_nothing(self):
        self.now_to_return(hour=13)
        self.actions_to_return([Action(type=WorkOptions.START, timestamp=datetime(2021, 1, 1, 12, 34, 56))])

        view: InfoView = self.handle([])

        self.assertEqual(self.fm.load_project.call_count, 3)
        self.assertEqual(self.fm.load_actions.call_count, 3)
        self.fm.save_actions.assert_not_called()
        self.assertEqual(view.value, "already started")
