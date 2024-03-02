from datetime import datetime

from forty.views import ActionView, InfoView, ErrorView
from forty.actions import Action, WorkOptions
from forty.controllers.finish import FinishController
from forty.tools import ActionsBuilder as A

from ..controller_test_case import ControllerTestCase


class TestFinishController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return FinishController

    def test_default(self):
        self.now_to_return()
        action_timestamp = datetime(year=2021, month=1, day=1)
        actions=[Action(type=WorkOptions.START, timestamp=action_timestamp)]
        self.actions_to_return(actions)

        view: ActionView = self.handle([])

        self.assertIsInstance(view, ActionView)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, action_timestamp)


        self.assertEqual(self.pm.load_project.call_count, 3)
        self.assertEqual(self.pm.load_actions.call_count, 3)
        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], Action(type=WorkOptions.FINISH, timestamp=action_timestamp))
        
    def test_specific_time(self):
        self.now_to_return()
        actions = A().start().at().done()
        self.actions_to_return(actions)
        expected = Action(type=WorkOptions.FINISH, timestamp=datetime(2021, 1, 1, 12, 34, 56))

        view: ActionView = self.handle(["12:34:56"])

        self.assertIsInstance(view, ActionView)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 12, 34, 56))

        self.assertEqual(self.pm.load_project.call_count, 3)
        self.assertEqual(self.pm.load_actions.call_count, 3)
        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], expected )

    def test_do_nothing(self):
        self.now_to_return()
        actions = A().start().at().finish().at().done()
        self.actions_to_return(actions)

        view: InfoView = self.handle([])

        self.assertIsInstance(view, InfoView)
        self.assertEqual(view.value, "already finished")

        self.assertEqual(self.pm.load_project.call_count, 3)
        self.assertEqual(self.pm.load_actions.call_count, 3)
        self.pm.save_actions.assert_not_called()

    def test_last_day_is_not_finished(self):
        actions = A().start().at().done()
        self.now_to_return(day=2)
        self.actions_to_return(actions)

        view: ErrorView = self.handle([])

        self.assertIsInstance(view, ErrorView)
        self.assertEqual(view.value, "invalid state at 2021-01-01")

        self.assertEqual(self.pm.load_project.call_count, 5)
        self.assertEqual(self.pm.load_actions.call_count, 5)
        self.assertEqual(self.pm.save_actions.call_count, 2)

    def test_specify_date(self):
        actions = A().start().at().done()
        self.now_to_return(day=1)
        self.actions_to_return(actions)
        expected = Action(type=WorkOptions.FINISH, timestamp=datetime(2021, 1, 1, 10, 0, 0))

        view: ActionView = self.handle(["2021-01-01", "10:00:00"])

        self.assertIsInstance(view, ActionView)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 10, 0, 0))

        self.assertEqual(self.pm.load_project.call_count, 3)
        self.assertEqual(self.pm.load_actions.call_count, 3)
        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], expected)

    def test_last_day_is_not_finished_specify_date(self):
        actions = A().start().at().done()
        self.now_to_return(day=2)
        self.actions_to_return(actions)
        expected = Action(type=WorkOptions.FINISH, timestamp=datetime(2021, 1, 1, 10, 0, 0))

        view: ActionView = self.handle(["2021-01-01", "10:00:00"])

        self.assertIsInstance(view, ActionView)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 10, 0, 0))

        self.assertEqual(self.pm.load_project.call_count, 3)
        self.assertEqual(self.pm.load_actions.call_count, 3)
        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], expected)
