from forty.handlers import ResetHandler

from .handler_test_case import HandlerTestCase


class TestResetHangler(HandlerTestCase):
    def __init__(self, *args, **kwargs):
        HandlerTestCase.__init__(self, *args, **kwargs)

    @property
    def handler_class(self):
        return ResetHandler

    def test_default(self):
        self.handle([])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_called_once_with([])
        self.om.emmit.assert_called_once_with("all actions are deleted")
