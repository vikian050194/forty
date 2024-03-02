from forty.actions import WorkOptions
from forty.views.status import OnlyStatusView
from forty.tools import ActionsBuilder as A
from forty.controllers.status.internal import StatusOnlyController

from ..controller_test_case import ControllerTestCase


class TestStatusOnlyController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusOnlyController


    def test_status(self):
        view: OnlyStatusView = self.handle([])

        self.assertEqual(view.status, None)

    def test_status_started(self):
        self.now_to_return()
        actions = A().start().at().done()
        self.actions_to_return(actions)

        view: OnlyStatusView = self.handle([])

        self.assertEqual(view.status, WorkOptions.START)

    def test_status_finished(self):
        self.now_to_return()
        actions = A().finish().at().done()
        self.actions_to_return(actions)

        view: OnlyStatusView = self.handle([])

        self.assertEqual(view.status, WorkOptions.FINISH)
