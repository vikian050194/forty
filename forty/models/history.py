from .base import AbstractModel


class HistoryModel(AbstractModel):
    def log(self):
        self.pm.load_project()
        actions = self.pm.load_actions()
        return actions

    def reset(self):
        self.pm.load_project()
        self.pm.save_actions([])

    def undo(self, count = 1):
        self.pm.load_project()
        actions = self.pm.load_actions()
        if actions:
            current_actions_count = len(actions)
            target_actions_delta = count
            if current_actions_count < target_actions_delta:
                target_actions_delta = current_actions_count
            index = 0 - target_actions_delta
            self.pm.save_actions(actions[:index])
            return target_actions_delta
        return 0


__all__ = ["HistoryModel"]
