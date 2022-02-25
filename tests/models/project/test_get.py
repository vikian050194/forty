from forty.models import ProjectModel

from ..model_test_case import ModelTestCase


class TestProjectModelGetMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return ProjectModel

    def test_non_exists(self):
        self.project_to_return(None)

        view: str = self.model.get()

        self.assertEqual(view, None)

    def test_project_exists(self):
        self.project_to_return("test")

        view: str = self.model.get()

        self.assertEqual(view, "test")
