from .base import AbstractModel


class ResetModel(AbstractModel):
    def reset(self):
        self.pm.load_project()
        self.pm.save_actions([])


__all__ = ["ResetModel"]
