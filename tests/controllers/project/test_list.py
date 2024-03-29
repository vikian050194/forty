from forty.views import ListView, InfoView
from forty.controllers.project.internal import ProjectListController

from ..controller_test_case import ControllerTestCase


class TestProjectListController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectListController

    def test_list_no_projects(self):
        self.projects_to_return([])

        view: InfoView = self.handle([])

        self.pm.load_project.assert_not_called()
        self.pm.get_projects_list.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "there are no projects")

    def test_list_few_projects(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])
        
        view: ListView = self.handle([])

        self.pm.load_project.assert_not_called()
        self.pm.get_projects_list.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertListEqual(view.list, ["aaa", "bbb", "ccc"])
