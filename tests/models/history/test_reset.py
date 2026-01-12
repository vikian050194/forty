from forty.models import HistoryModel

from ..model_test_case import ModelTestCase


class TestHistoryModelResetMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def model_class(self):
        return HistoryModel

    def test_call(self):
        self.project_to_return(None)

        view: str = self.model.reset()

        self.assertEqual(view, None)
        self.fm.load_project.assert_called_once()
        self.fm.save_actions.assert_called_with([])
