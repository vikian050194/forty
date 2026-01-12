from forty.models import HistoryModel

from ..model_test_case import ModelTestCase


class TestHistoryModelLogMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def model_class(self):
        return HistoryModel

    def test_no_actions(self):
        self.actions_to_return([])

        view: str = self.model.log()

        self.assertEqual(view, [])
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()

    def test_few_actions(self):
        self.actions_to_return(["a", "b", "c"])

        view: str = self.model.log()

        self.assertEqual(view, ["a", "b", "c"])
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
