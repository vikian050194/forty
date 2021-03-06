from forty.views.base import StrView, ListView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController

from ..controller_test_case import ControllerTestCase


class TestStatusControllerTodayCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    def test_today_started(self):
        self.now_to_return(hour=14, minute=15, second=16)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["today"])

        self.assertListEqual(view.list, ["06:15:16", "01:44:44"])

    def test_today_started_overtime(self):
        self.now_to_return(hour=16, minute=17, second=18)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["today"])

        self.assertListEqual(view.list, ["08:17:18", "-00:17:18"])
