from forty.views import ActionView, StrView
from forty.actions import Action, WorkOptions
from forty.controllers import WorkController
from forty.tools import ActionsBuilder as A

from ..controller_test_case import ControllerTestCase


class TestWorkControllerFinishCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return WorkController

    def test_default(self):
        actions = A().start().done()
        self.actions_to_return(actions)
        timestamp = self.tm.get_datetime()

        view: ActionView = self.handle(["work", "finish"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], Action(type=WorkOptions.FINISH, timestamp=timestamp))
        self.assertEqual(view.action.type, WorkOptions.FINISH)
        self.assertEqual(view.action.timestamp, timestamp)

    def test_specific_time(self):
        actions = A().start().done()
        self.actions_to_return(actions)
        timestamp = self.tm.merge_time()
        
        view: ActionView = self.handle(["work", "finish", "12:34:56"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], Action(type=WorkOptions.FINISH, timestamp=timestamp))
        self.assertEqual(view.action.type, WorkOptions.FINISH)
        self.assertEqual(view.action.timestamp, timestamp)

    def test_do_nothing(self):
        self.actions_to_return([Action(type=WorkOptions.FINISH, timestamp=None)])

        view: StrView = self.handle(["work", "finish"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "already finished")
