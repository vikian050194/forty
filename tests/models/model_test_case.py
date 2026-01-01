from unittest import TestCase
from unittest.mock import create_autospec, Mock

from datetime import datetime, date

from forty.managers.file_manager import AbstractFileManager, Config, FileManager
from forty.managers.time_manager import AbstractTimeManager, TimeManager
from forty.models.base import AbstractModel


def get_project_manager_spec():
    fm: AbstractFileManager = create_autospec(spec=FileManager, spec_set=True, instance=True)
    return fm


class ModelTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

        self.fm: AbstractFileManager = get_project_manager_spec()
        self.tm: AbstractTimeManager = TimeManager()

        self.model = self.model_class(fm=self.fm, tm=self.tm)

    def setUp(self):
        self.fm.reset_mock()
        self.fm.load_project = Mock(return_value="test_project")
        self.fm.load_actions = Mock(return_value=[])
        config = Config(day_limit=8, total_limit=40)
        config.today = date(year=2021, month=1, day=1)
        self.fm.load_config = Mock(return_value=config)

    def tearDown(self):
        pass

    @property
    def model_class(self) -> AbstractModel:
        raise NotImplementedError()

    def project_to_return(self, project):
        self.fm.load_project = Mock(return_value=project)

    def projects_to_return(self, projects):
        self.fm.get_projects_list = Mock(return_value=projects)

    def config_to_return(self, config):
        self.fm.load_config = Mock(return_value=config)

    def actions_to_return(self, actions):
        self.fm.load_actions = Mock(return_value=actions)

    def now_to_return(self, year=2021, month=1, day=1, hour=0, minute=0, second=0):
        datetime_value = datetime(year, month, day, hour, minute, second)
        self.tm.get_datetime = Mock(return_value=datetime_value)


__all__ = ["ModelTestCase"]
