import abc
import enum
import subprocess


@enum.unique
class UrgencyLevel(str, enum.Enum):
    LOW = "low"
    NORMAL = "normal"
    CRITICAL = "critical"


def send_message(body: str, expire_time: int = 10):
    urgency: UrgencyLevel = UrgencyLevel.NORMAL
    # icon = dir + "icon.png"
    title = "forty"
    body = body.replace("-", "\-")
    arguments = ['notify-send']
    arguments.append(title)
    arguments.append(body)
    arguments.append(f"--expire-time={expire_time * 1000}")
    arguments.append(f"--urgency={urgency}")
    # arguments.append(f"--icon={icon}")
    arguments.append("--hint=int:transient:1")
    # arguments.append("--app-name=forty")
    subprocess.Popen(arguments)


class AbstractOutputManager(abc.ABC):
    @abc.abstractmethod
    def emmit(self,  message: str, use_print: bool = True, use_notify: bool = False):
        raise NotImplementedError()


class OutputManager():
    def __init__(self, use_print: bool = True, use_notify: bool = False):
        self.use_print = use_print
        self.use_notify = use_notify

    def __notify(self, message):
        send_message(message)

    def __print(self, message):
        return print(message)

    def emmit(self,  message: str, use_print: bool = True, use_notify: bool = False):
        if self.use_print or use_print:
            self.__print(message)
        if self.use_notify or use_notify:
            self.__notify(message)


__all__ = ["OutputManager"]
