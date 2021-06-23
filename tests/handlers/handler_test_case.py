from unittest import TestCase
from unittest.mock import create_autospec, Mock, MagicMock

from datetime import datetime

from forty.common import from_iso
from forty.managers.project_manager import AbstractProjectManager, Config, ProjectManager
from forty.managers.output_manager import AbstractOutputManager, OutputManager
from forty.managers.time_manager import AbstractTimeManager, TimeManager


class HandlerTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

        self.pm: AbstractProjectManager = create_autospec(spec=ProjectManager, spec_set=True, instance=True)
        # pm: AbstractProjectManager = Mock(spec=ProjectManager, spec_set=True)
        # pm: AbstractProjectManager = MagicMock(spec=ProjectManager, spec_set=True)

        self.om: AbstractOutputManager = create_autospec(spec=OutputManager, spec_set=True, instance=True)
        # om: AbstractOutputManager = Mock(spec=OutputManager, spec_set=True)
        # om: AbstractOutputManager = MagicMock(spec=OutputManager, spec_set=True)

        self.tm: AbstractTimeManager = create_autospec(spec=TimeManager, spec_set=True, instance=True)
        # tm: AbstractTimeManager = Mock(spec=TimeManager, spec_set=True)
        # tm: AbstractTimeManager = MagicMock(spec=TimeManager, spec_set=True)

        handler = self.handler_class(pm=self.pm, om=self.om, tm=self.tm)
        self.handle = handler.handle

    def setUp(self):
        self.pm.reset_mock()
        self.pm.load_project = Mock(return_value="test_project")
        self.pm.load_actions = Mock(return_value=[])
        config = Config(day_limit=8, total_limit=40)
        config.today = "2021-01-01"
        self.pm.load_config = Mock(return_value=config)
    
        self.om.reset_mock()

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
    def handler_class(self):
        raise NotImplementedError()

    def project_to_return(self, project):
        self.pm.load_project = Mock(return_value=project)

    def config_to_return(self, config):
        self.pm.load_config = Mock(return_value=config)

    def actions_to_return(self, actions):
        self.pm.load_actions = Mock(return_value=actions)

    def now_to_return(self, year=2021, month=1, day=1, hour=0, minute=0, second=0):
        now = datetime(year, month, day, hour, minute, second)
        self.tm.get_datetime = Mock(return_value=now)


__all__ = ["HandlerTestCase"]
