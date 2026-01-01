from datetime import date

from forty.tools import ActionsBuilder as A
from forty.views import ListView, InfoView
from forty.controllers.date import DateController

from ..controller_test_case import ControllerTestCase


class TestDateController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return DateController

    def test_no_actions(self):
        view: InfoView = self.handle([])

        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_not_called()
        self.assertEqual(view.value, "there are no dates")

    def test_one_day(self):
        actions = A().start().at().finish().at().done()
        self.actions_to_return(actions)

        view: ListView = self.handle([])

        self.assertEqual(len(view.list), 1)
        self.assertListEqual(view.list, [date(year=2021, month=1, day=1)])
