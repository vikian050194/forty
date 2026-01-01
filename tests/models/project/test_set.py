from forty.models import ProjectModel

from ..model_test_case import ModelTestCase


class TestProjectModelSetMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return ProjectModel

    def test_non_exists(self):
        self.projects_to_return([])

        view: str = self.model.set("test")

        self.assertEqual(view, None)
        self.fm.select_project.assert_not_called()
        self.fm.save_project.assert_not_called()

    def test_exists(self):
        self.projects_to_return(["test"])

        view: str = self.model.set("test")

        self.assertEqual(view, "test")
        self.fm.select_project.assert_called_with("test")
        self.fm.save_project.assert_called_once()
