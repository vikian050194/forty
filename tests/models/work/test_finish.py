from datetime import datetime, date, time

from forty.actions import Action, WorkOptions
from forty.models import WorkModel
from forty.tools import ActionsBuilder as A

from ..model_test_case import ModelTestCase


class TestWorkModelFinishMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def model_class(self):
        return WorkModel

    def test_no_actions(self):
        self.actions_to_return([])

        view: Action = self.model.finish()

        self.assertEqual(view, None)
        
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_not_called()

    # TODO refactoring
    def test_current_date_and_time(self):
        self.now_to_return(hour=8, minute=12, second=34)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)
        expected = Action(WorkOptions.FINISH, datetime(2021, 1, 1, 8, 12, 34), None)

        view: Action = self.model.finish()

        self.assertEqual(view.value, None)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 8, 12, 34))
        
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_called_once()
        args, _ = self.fm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], expected)

    # TODO refactoring
    def test_custom_time(self):
        self.now_to_return()
        actions = A().start().at().done()
        self.actions_to_return(actions)
        finish_time = time(hour=12, minute=23, second=34)
        expected = Action(WorkOptions.FINISH, datetime(2021, 1, 1, 12, 23, 34), None)

        view: Action = self.model.finish(new_time=finish_time)

        self.assertEqual(view.value, None)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 1, 1, 12, 23, 34))
        
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_called_once()
        args, _ = self.fm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], expected)

    # TODO refactoring
    def test_custom_date(self):
        self.now_to_return()
        actions = A().start().at().done()
        self.actions_to_return(actions)
        finish_date = date(year=2021, month=2, day=2)
        expected = Action(WorkOptions.FINISH, datetime(2021, 2, 2, 0, 0, 0), None)

        view: Action = self.model.finish(new_date=finish_date)

        self.assertEqual(view.value, None)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 2, 2, 0, 0, 0))
        
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_called_once()
        args, _ = self.fm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], expected)

    # TODO refactoring
    def test_custom_date_and_time(self):
        self.now_to_return()
        actions = A().start().at().done()
        self.actions_to_return(actions)
        finish_date = date(year=2021, month=2, day=2)
        finish_time = time(hour=12, minute=23, second=34)
        expected = Action(WorkOptions.FINISH, datetime(2021, 2, 2, 12, 23, 34), None)

        view: Action = self.model.finish(new_date=finish_date, new_time=finish_time)

        self.assertEqual(view.value, None)
        self.assertEqual(view.type, WorkOptions.FINISH)
        self.assertEqual(view.timestamp, datetime(2021, 2, 2, 12, 23, 34))
        
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_called_once()
        args, _ = self.fm.save_actions.call_args_list[0]
        (updated_actions,) = args
        self.assertEqual(len(updated_actions), 2)
        self.assertEqual(updated_actions[0], actions[0])
        self.assertEqual(updated_actions[1], expected)

    # TODO refactoring
    def test_already_finished(self):
        actions = A().start().finish().done()
        self.actions_to_return(actions)
        view: Action = self.model.finish()

        self.assertEqual(view, None)
        
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_not_called()
