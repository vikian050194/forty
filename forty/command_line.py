#!/usr/bin/env python3

from os import environ
from sys import argv
from pathlib import Path

import forty


def main():
    home = Path.home().as_posix()
    home = environ.get("FORTY_HOME", home)
    env_options = {}
    use_print = environ.get("FORTY_PRINT", None)
    if not use_print in None:
        env_options["use_print"] = use_print
    use_notify = environ.get("FORTY_NOTIFY", None)
    if not use_notify in None:
        env_options["use_notify"] = use_notify
    options = argv[1:]
    forty.main(home=home, options=options, **env_options)
