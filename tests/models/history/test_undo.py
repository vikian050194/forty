from forty.models import HistoryModel

from ..model_test_case import ModelTestCase


class TestHistoryModelUndoMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def model_class(self):
        return HistoryModel

    def test_no_actions(self):
        self.actions_to_return([])

        view: int = self.model.undo()

        self.assertEqual(view, 0)
        self.fm.load_project.assert_called_once()
        self.fm.save_actions.assert_not_called()

    def test_default_count(self):
        self.actions_to_return(["a", "b", "c"])

        view: int = self.model.undo()

        self.assertEqual(view, 1)
        self.fm.load_project.assert_called_once()
        self.fm.save_actions.assert_called_with(["a", "b"])

    def test_undo_two(self):
        self.actions_to_return(["a", "b", "c"])

        view: int = self.model.undo(2)

        self.assertEqual(view, 2)
        self.fm.load_project.assert_called_once()
        self.fm.save_actions.assert_called_with(["a"])

    def test_undo_four(self):
        self.actions_to_return(["a", "b", "c"])

        view: int = self.model.undo(4)

        self.assertEqual(view, 3)
        self.fm.load_project.assert_called_once()
        self.fm.save_actions.assert_called_with([])
