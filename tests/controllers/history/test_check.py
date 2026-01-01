from forty.tools import ActionsBuilder as A
from forty.views import ListView, StrView, InfoView
from forty.controllers.check import CheckController

from ..controller_test_case import ControllerTestCase


class TestCheckController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return CheckController

    def test_one_day_no_actions(self):
        view: StrView = self.handle(["2021-01-01"])

        self.assertIsInstance(view, StrView)
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.assertEqual(view.value, "2021-01-01 is OK")

    def test_one_day_not_finished(self):
        actions = A().start().at().done()
        self.actions_to_return(actions)

        view: StrView = self.handle(["2021-01-01"])

        self.assertIsInstance(view, StrView)
        self.assertEqual(view.value, "2021-01-01 is bad")

    def test_one_day_finished(self):
        actions = A().start().at().finish().at().done()
        self.actions_to_return(actions)

        view: StrView = self.handle(["2021-01-01"])

        self.assertIsInstance(view, StrView)
        self.assertEqual(view.value, "2021-01-01 is OK")

    def test_all_days_no_actions(self):
        view: InfoView = self.handle([])

        self.assertIsInstance(view, InfoView)
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.assertEqual(view.value, "there is nothing to check")

    def test_all_days_not_finished(self):
        actions = A().start().at().done()
        self.actions_to_return(actions)

        view: ListView = self.handle([])

        self.assertIsInstance(view, ListView)
        self.assertEqual(view.list, ["2021-01-01 is bad"])

    def test_all_days_finished(self):
        actions = A().start().at().finish().at().done()
        self.actions_to_return(actions)

        view: ListView = self.handle([])

        self.assertIsInstance(view, ListView)
        self.assertEqual(view.list, ["2021-01-01 is OK"])

    def test_all_days_two_finished(self):
        actions = (A()
            .start().at(day=1)
            .finish().at(day=1)
            .start().at(day=2)
            .finish().at(day=2)
            .done())
        self.actions_to_return(actions)

        view: ListView = self.handle([])

        self.assertIsInstance(view, ListView)
        self.assertEqual(view.list, ["2021-01-01 is OK", "2021-01-02 is OK"])

    def test_all_days_last_not_finished(self):
        actions = (A()
            .start().at(day=1)
            .finish().at(day=1)
            .start().at(day=2)
            .done())
        self.actions_to_return(actions)

        view: ListView = self.handle([])

        self.assertIsInstance(view, ListView)
        self.assertEqual(view.list, ["2021-01-01 is OK", "2021-01-02 is bad"])
