from unittest import skip
from forty.views import AbstractView, StrView, ListView
from forty.controllers import ProjectController

from ..controller_test_case import ControllerTestCase


class TestProjectController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectController

    def test_default(self):
        view: AbstractView = self.handle(["project"])

        self.pm.load_project.assert_not_called()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_not_called()
        self.assertIsNone(view)

    def test_get(self):
        view: StrView = self.handle(["project", "get"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "test_project")

    def test_list_no_projects(self):
        self.projects_to_return([])
        # TODO should return message
        view: ListView = self.handle(["project", "list"])

        self.pm.load_project.assert_not_called()
        self.pm.get_projects_list.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertListEqual(view.list, [])

    def test_list_few_projects(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])
        
        view: ListView = self.handle(["project", "list"])

        self.pm.load_project.assert_not_called()
        self.pm.get_projects_list.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertListEqual(view.list, ["aaa", "bbb", "ccc"])

    @skip("not implemented")
    def test_new_missed_name(self):
        view: StrView = self.handle(["project", "new"])

        self.assertEqual(view.value, "new project name is not specified")

    @skip("not implemented")
    def test_new_not_unique_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "new", "aaa"])

        self.assertEqual(view.value, "new project name should be unique")

    def test_new(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "new", "ddd"])

        self.assertEqual(view.value, "ddd")

    def test_set_wrong_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "set", "ddd"])

        self.assertEqual(view.value, "project ddd is not found")

    def test_set_correct_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "set", "aaa"])

        self.assertEqual(view.value, "aaa")
