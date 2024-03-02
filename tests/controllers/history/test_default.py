# from forty.controllers import HistoryController
# from forty.views.base import AbstractView

# from ..controller_test_case import ControllerTestCase


# class TestHistoryControllerDefaultCommand(ControllerTestCase):
#     def __init__(self, *args, **kwargs):
#         ControllerTestCase.__init__(self, *args, **kwargs)

#     @property
#     def controller_class(self):
#         return HistoryController

#     def test_default(self):
#         view: AbstractView = self.handle(["history"])

#         self.pm.load_project.assert_not_called()
#         self.pm.load_actions.assert_not_called()
#         self.pm.save_actions.assert_not_called()
#         self.assertIsNone(view)