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

        view: ActionView = self.handle(["work", "start"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.pm.save_actions.assert_called_once_with([Action(type=WorkOptions.START, timestamp=timestamp)])
        self.assertEqual(view.action.type, WorkOptions.START)
        self.assertEqual(view.action.timestamp, timestamp)

    def test_specific_time(self):
        timestamp = self.tm.merge_time()
        
        view: ActionView = self.handle(["work", "start", "12:34:56"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.pm.save_actions.assert_called_once_with([Action(type=WorkOptions.START, timestamp=timestamp)])
        self.assertEqual(view.action.type, WorkOptions.START)
        self.assertEqual(view.action.timestamp, timestamp)

    def test_do_nothing(self):
        self.actions_to_return([Action(type=WorkOptions.START, timestamp=None)])

        view: InfoView = self.handle(["work", "start"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "already started")
