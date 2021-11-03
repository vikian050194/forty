from datetime import date

from forty.views.base import ListView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController
from forty.managers.project_manager import Config

from ..controller_test_case import ControllerTestCase


class TestStatusControllerTillCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    def test_today_not_started(self):
        actions = A().done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["till"])

        self.assertListEqual(view.list, [None])

    def test_today_started_till_today(self):
        self.now_to_return(hour=12, minute=34, second=56)
        actions = A().start().at(hour=9).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["till"])

        self.assertListEqual(view.list, ["17:00:00"])

    def test_whatsup_started_till_today_overtime(self):
        self.now_to_return(day=1, hour=19)
        actions = A().start().at(day=1,hour=9).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["till"])

        self.assertListEqual(view.list, ["17:00:00"])

    # TODO should I change this behavior?
    def test_today_started_till_tomorrow(self):
        self.now_to_return(hour=21, minute=22, second=23)
        actions = A().start().at(hour=20, minute=30, second=40).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["till"])

        self.assertListEqual(view.list, ["04:30:40"])

    def test_today_finished(self):
        self.now_to_return(hour=10, minute=11, second=12)
        actions = A().start().at(hour=8).finish().at(hour=9).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["till"])

        self.assertListEqual(view.list, [None])
