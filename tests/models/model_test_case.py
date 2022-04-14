from unittest import TestCase
from unittest.mock import create_autospec, Mock

from datetime import datetime, date

from forty.managers.project_manager import AbstractProjectManager, Config, ProjectManager
from forty.managers.time_manager import AbstractTimeManager, TimeManager
from forty.models.base import AbstractModel


def get_project_manager_spec():
    pm: AbstractProjectManager = create_autospec(spec=ProjectManager, spec_set=True, instance=True)
    return pm


class ModelTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

        self.pm: AbstractProjectManager = get_project_manager_spec()
        self.tm: AbstractTimeManager = TimeManager()

        self.model = self.model_class(pm=self.pm, tm=self.tm)

    def setUp(self):
        self.pm.reset_mock()
        self.pm.load_project = Mock(return_value="test_project")
        self.pm.load_actions = Mock(return_value=[])
        config = Config(day_limit=8, total_limit=40)
        config.today = date(year=2021, month=1, day=1)
        self.pm.load_config = Mock(return_value=config)

    def tearDown(self):
        pass

    @property
    def model_class(self) -> AbstractModel:
        raise NotImplementedError()

    def project_to_return(self, project):
        self.pm.load_project = Mock(return_value=project)

    def projects_to_return(self, projects):
        self.pm.get_projects_list = Mock(return_value=projects)

    def config_to_return(self, config):
        self.pm.load_config = Mock(return_value=config)

    def actions_to_return(self, actions):
        self.pm.load_actions = Mock(return_value=actions)

    def now_to_return(self, year=2021, month=1, day=1, hour=0, minute=0, second=0):
        datetime_value = datetime(year, month, day, hour, minute, second)
        self.tm.get_datetime = Mock(return_value=datetime_value)


__all__ = ["ModelTestCase"]
