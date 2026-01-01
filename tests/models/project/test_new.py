from forty.models import ProjectModel

from ..model_test_case import ModelTestCase


class TestProjectModelNewMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return ProjectModel

    def test_new_one(self):
        self.projects_to_return([])

        view: str = self.model.new("test")

        self.assertEqual(view, "test")
        self.fm.initialize_new_project.assert_called_with("test")

    def test_already_exists(self):
        self.projects_to_return(["test"])

        view: str = self.model.new("test")

        self.assertEqual(view, None)
        self.fm.initialize_new_project.assert_not_called()
