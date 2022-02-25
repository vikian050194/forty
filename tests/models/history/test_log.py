from forty.models import HistoryModel

from ..model_test_case import ModelTestCase


class TestHistoryModelLogMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return HistoryModel

    def test_no_actions(self):
        self.actions_to_return([])

        view: str = self.model.log()

        self.assertEqual(view, [])
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_few_actions(self):
        self.actions_to_return(["a", "b", "c"])

        view: str = self.model.log()

        self.assertEqual(view, ["a", "b", "c"])
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
