from forty.tools import ActionsBuilder as A
from forty.handlers import GetHandler

from .handler_test_case import HandlerTestCase


class TestGetHangler(HandlerTestCase):
    def __init__(self, *args, **kwargs):
        HandlerTestCase.__init__(self, *args, **kwargs)

    @property
    def handler_class(self):
        return GetHandler

    def test_default(self):
        self.handle([])

        self.pm.load_project.assert_called_once()
        self.pm.load_config.assert_called_once()
        self.pm.load_actions.assert_called_once()

        self.om.emmit.assert_called_once_with("test_project/noned/00:00:00/08:00:00/00:00:00/40:00:00")

    def test_status(self):
        self.handle(["status"])

        self.om.emmit.assert_called_once_with("test_project/noned")

    def test_status_started(self):
        actions = A().start().done()
        self.actions_to_return(actions)

        self.handle(["status"])

        self.om.emmit.assert_called_once_with("test_project/started")

    def test_status_finished(self):
        actions = A().finish().done()
        self.actions_to_return(actions)

        self.handle(["status"])

        self.om.emmit.assert_called_once_with("test_project/finished")

    def test_all(self):
        self.handle(["all"])

        self.om.emmit.assert_called_once_with("test_project/noned/00:00:00/08:00:00/00:00:00/40:00:00")

    def test_all_started(self):
        self.now_to_return(hour=12, minute=34, second=56)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        self.handle(["all"])

        self.om.emmit.assert_called_once_with("test_project/started/04:34:56/03:25:04/04:34:56/35:25:04")

    def test_all_started_today_overtime(self):
        self.now_to_return(day=1, hour=9, minute=8, second=7)
        actions = A().start().at().done()
        self.actions_to_return(actions)

        self.handle(["all"])

        self.om.emmit.assert_called_once_with("test_project/started/09:08:07/-01:08:07/09:08:07/30:51:53")

    def test_all_finished_total_overtime(self):
        actions = (A()
            .start().at(day=1,hour=0)
            .finish().at(day=1, hour=23)
            .start().at(day=2,hour=0)
            .finish().at(day=2, hour=23)
            .done())
        self.actions_to_return(actions)

        self.handle(["all"])

        self.om.emmit.assert_called_once_with("test_project/finished/23:00:00/-15:00:00/46:00:00/-06:00:00")

    def test_all_finished(self):
        self.now_to_return(hour=18, minute=0, second=0)
        actions = A().start().at(hour=8).finish().at(hour=12, minute=34, second=56).done()
        self.actions_to_return(actions)

        self.handle(["all"])

        self.om.emmit.assert_called_once_with("test_project/finished/04:34:56/03:25:04/04:34:56/35:25:04")

    def test_today(self):
        self.handle(["today"])

        self.om.emmit.assert_called_once_with("test_project/noned/00:00:00/08:00:00")

    def test_today_started(self):
        self.now_to_return(hour=14, minute=15, second=16)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        self.handle(["today"])

        self.om.emmit.assert_called_once_with("test_project/started/06:15:16/01:44:44")

    def test_today_started_overtime(self):
        self.now_to_return(hour=16, minute=17, second=18)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        self.handle(["today"])

        self.om.emmit.assert_called_once_with("test_project/started/08:17:18/-00:17:18")

    def test_total(self):
        self.handle(["total"])

        self.om.emmit.assert_called_once_with("test_project/noned/00:00:00/40:00:00")

    def test_total_started(self):
        self.now_to_return(hour=19, minute=33, second=42)
        actions = A().start().at(hour=9).done()
        self.actions_to_return(actions)

        self.handle(["total"])

        self.om.emmit.assert_called_once_with("test_project/started/10:33:42/29:26:18")

    def test_total_started_overtime(self):
        self.now_to_return(day=3,hour=3, minute=4, second=5)
        actions = A().start().at(day=1, hour=8).done()
        self.actions_to_return(actions)

        self.handle(["total"])

        self.om.emmit.assert_called_once_with("test_project/started/43:04:05/-03:04:05")

    def test_passed(self):
        self.handle(["passed"])

        self.om.emmit.assert_called_once_with("test_project/noned/00:00:00/00:00:00")

    def test_remained(self):
        self.handle(["remained"])

        self.om.emmit.assert_called_once_with("test_project/noned/08:00:00/40:00:00")
