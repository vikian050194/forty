from unittest import TestCase
from unittest.mock import create_autospec, Mock, MagicMock

from datetime import datetime, date, time

from forty.managers.project_manager import AbstractProjectManager, Config, ProjectManager
from forty.managers.time_manager import AbstractTimeManager, TimeManager
from forty.models.base import AbstractModel


def get_project_manager_spec():
    pm: AbstractProjectManager = create_autospec(spec=ProjectManager, spec_set=True, instance=True)
    # pm: AbstractProjectManager = Mock(spec=ProjectManager, spec_set=True)
    # pm: AbstractProjectManager = MagicMock(spec=ProjectManager, spec_set=True)
    return pm


def get_time_manager_spec():
    tm: AbstractTimeManager = create_autospec(spec=TimeManager, spec_set=True, instance=True)
    # tm: AbstractTimeManager = Mock(spec=TimeManager, spec_set=True)
    # tm: AbstractTimeManager = MagicMock(spec=TimeManager, spec_set=True)
    return tm


class ModelTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

        self.pm: AbstractProjectManager = get_project_manager_spec()
        self.tm: AbstractTimeManager = get_time_manager_spec()

        self.model = self.model_class(pm=self.pm, tm=self.tm)

    def setUp(self):
        self.pm.reset_mock()
        self.pm.load_project = Mock(return_value="test_project")
        self.pm.load_actions = Mock(return_value=[])
        config = Config(day_limit=8, total_limit=40)
        config.today = date(year=2021, month=1, day=1)
        self.pm.load_config = Mock(return_value=config)
    
        self.tm.reset_mock()
        timestamp_now: datetime = create_autospec(spec=datetime, spec_set=True, instance=True)
        timestamp_now.isoformat = Mock(return_value="test_time_now")
        self.tm.get_datetime = Mock(return_value=timestamp_now)
        timestamp_merge: datetime = create_autospec(spec=datetime, spec_set=True, instance=True)
        timestamp_merge.isoformat = Mock(return_value="test_time_merge")
        self.tm.merge_time = Mock(return_value=timestamp_merge)

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
        date_value = date(year, month, day)
        self.tm.get_date = Mock(return_value=date_value)
        time_value = time(hour, minute, second)
        self.tm.get_time = Mock(return_value=time_value)


__all__ = ["ModelTestCase"]
