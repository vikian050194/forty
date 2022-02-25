from datetime import datetime, time
from unittest.mock import Mock

from forty.actions import Action, WorkOptions
from forty.models import WorkModel
from forty.tools import ActionsBuilder as A

from ..model_test_case import ModelTestCase


class TestWorkModelFinishMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return WorkModel

    def test_no_actions(self):
        self.actions_to_return([])

        view: Action = self.model.finish()

        self.assertEqual(view, None)
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()

    # TODO refactoring
    def test_three_actions_custom_time(self):
        actions = A().start().finish().start().done()
        self.actions_to_return(actions)
        self.tm.merge_time = Mock(return_value=datetime(2021, 1, 1, 8, 12, 34))
        start_time: time = time(hour=8, minute=12, second=34)
        expected = Action(WorkOptions.FINISH, datetime(2021, 1, 1, 8, 12, 34), None)

        view: Action = self.model.finish(start_time)

        self.assertEqual(view.value, None)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 8, 12, 34))
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once()
        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 4)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], actions[1])
        self.assertEqual(updated_actions[2], actions[2])
        self.assertEqual(updated_actions[3], expected)

    # TODO refactoring
    def test_already_finished(self):
        actions = A().start().finish().done()
        self.actions_to_return(actions)
        view: Action = self.model.finish()

        self.assertEqual(view, None)
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
