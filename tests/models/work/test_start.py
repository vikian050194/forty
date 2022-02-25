from datetime import datetime, time
from unittest.mock import Mock

from forty.actions import Action, WorkOptions
from forty.models import WorkModel
from forty.tools import ActionsBuilder as A

from ..model_test_case import ModelTestCase


class TestWorkModelStartMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return WorkModel

    # TODO refactoring
    def test_no_actions_default_time(self):
        self.actions_to_return([])
        self.now_to_return(hour=8, minute=12, second=34)
        expected = Action(WorkOptions.START, datetime(2021, 1, 1, 8, 12, 34), None)

        view: Action = self.model.start()

        self.assertEqual(view.value, None)
        self.assertEqual(view.type, WorkOptions.START)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 8, 12, 34))
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once()
        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 1)
        self.assertEqual(updated_actions[0], expected)

    # TODO refactoring
    def test_two_actions_custom_time(self):
        actions = A().start().finish().done()
        self.actions_to_return(actions)
        self.tm.merge_time = Mock(return_value=datetime(2021, 1, 1, 8, 12, 34))
        start_time: time = time(hour=8, minute=12, second=34)
        expected = Action(WorkOptions.START, datetime(2021, 1, 1, 8, 12, 34), None)

        view: Action = self.model.start(start_time)

        self.assertEqual(view.value, None)
        self.assertEqual(view.type, WorkOptions.START)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 8, 12, 34))
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once()
        args, _ = self.pm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 3)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], actions[1])
        self.assertEqual(updated_actions[2], expected)

    def test_already_started(self):
        actions = A().start().done()
        self.actions_to_return(actions)
        view: Action = self.model.start()

        self.assertEqual(view, None)
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
