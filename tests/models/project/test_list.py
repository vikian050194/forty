from typing import List

from forty.models import ProjectModel

from ..model_test_case import ModelTestCase


class TestProjectModelListMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return ProjectModel

    def test_no_projects(self):
        self.projects_to_return([])

        view: List[str] = self.model.list()

        self.assertEqual(view, [])

    def test_three_projects(self):
        self.projects_to_return(["ccc", "aaa", "bbb"])

        view: List[str] = self.model.list()

        self.assertEqual(view, ["aaa", "bbb", "ccc"])
