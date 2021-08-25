from forty.views.base import StrView, ListView
from forty.tools import ActionsBuilder as A
from forty.controllers import GetController

from .controller_test_case import ControllerTestCase


class TestGetController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return GetController

    def test_default(self):
        view: ListView = self.handle([])

        self.pm.load_project.assert_called_once()
        self.pm.load_config.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.assertListEqual(view.list, ["00:00:00", "08:00:00", "00:00:00", "40:00:00"])

    def test_status(self):
        view: StrView = self.handle(["status"])

        self.assertEqual(view.value, "none")

    def test_status_started(self):
        actions = A().start().done()
        self.actions_to_return(actions)

        view: StrView = self.handle(["status"])

        self.assertEqual(view.value, "started")

    def test_status_finished(self):
        actions = A().finish().done()
        self.actions_to_return(actions)

        view: StrView = self.handle(["status"])

        self.assertEqual(view.value, "finished")

    def test_all(self):
        view: ListView = self.handle(["all"])

        self.assertListEqual(view.list, ["00:00:00", "08:00:00", "00:00:00", "40:00:00"])

    def test_all_started(self):
        self.now_to_return(hour=12, minute=34, second=56)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["all"])

        self.assertListEqual(view.list, ["04:34:56", "03:25:04", "04:34:56", "35:25:04"])

    def test_all_started_today_overtime(self):
        self.now_to_return(day=1, hour=9, minute=8, second=7)
        actions = A().start().at().done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["all"])

        self.assertListEqual(view.list, ["09:08:07", "-01:08:07", "09:08:07", "30:51:53"])

    def test_all_finished_total_overtime(self):
        actions = (A()
            .start().at(day=1,hour=0)
            .finish().at(day=1, hour=23)
            .start().at(day=2,hour=0)
            .finish().at(day=2, hour=23)
            .done())
        self.actions_to_return(actions)

        view: ListView = self.handle(["all"])

        self.assertListEqual(view.list, ["23:00:00", "-15:00:00", "46:00:00", "-06:00:00"])

    def test_all_finished(self):
        self.now_to_return(hour=18, minute=0, second=0)
        actions = A().start().at(hour=8).finish().at(hour=12, minute=34, second=56).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["all"])

        self.assertListEqual(view.list, ["04:34:56", "03:25:04", "04:34:56", "35:25:04"])

    def test_today(self):
        view: ListView = self.handle(["today"])

        self.assertListEqual(view.list, ["00:00:00", "08:00:00"])

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

    def test_total(self):
        view: ListView = self.handle(["total"])

        self.assertListEqual(view.list, ["00:00:00", "40:00:00"])

    def test_total_started(self):
        self.now_to_return(hour=19, minute=33, second=42)
        actions = A().start().at(hour=9).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["total"])

        self.assertListEqual(view.list, ["10:33:42", "29:26:18"])

    def test_total_started_overtime(self):
        self.now_to_return(day=3,hour=3, minute=4, second=5)
        actions = A().start().at(day=1, hour=8).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["total"])

        self.assertListEqual(view.list, ["43:04:05", "-03:04:05"])

    def test_passed(self):
        view: ListView = self.handle(["passed"])

        self.assertListEqual(view.list, ["00:00:00", "00:00:00"])

    def test_remained(self):
        view: ListView = self.handle(["remained"])

        self.assertListEqual(view.list, ["08:00:00", "40:00:00"])
