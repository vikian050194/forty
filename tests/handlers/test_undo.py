from forty.actions import Action, Actions
from forty.handlers import UndoHandler

from .handler_test_case import HandlerTestCase


class TestUndoHangler(HandlerTestCase):
    def __init__(self, *args, **kwargs):
        HandlerTestCase.__init__(self, *args, **kwargs)

    @property
    def handler_class(self):
        return UndoHandler

    def test_default(self):
        self.actions_to_return(["one", "two", "three"])

        self.handle([])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once_with(["one", "two"])
        self.om.emmit.assert_called_once_with("last 1 action is deleted")

    def test_two_actions(self):
        self.actions_to_return(["one", "two", "three"])

        self.handle(["2"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once_with(["one"])
        self.om.emmit.assert_called_once_with("last 2 actions are deleted")
