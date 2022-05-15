#!/usr/bin/env python3

from os import environ
from sys import argv

from forty import main
from forty.configuration import make_config


if __name__ == "__main__":
    home = environ.get("FORTY_HOME", None)
    output = environ.get("FORTY_OUTPUT", None)
    status = environ.get("FORTY_STATUS", None)

    configuration = make_config(home=home, output=output, status=status)

    options = argv[1:]
    main(options=options, configuration=configuration)
