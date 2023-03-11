from os import environ
from sys import argv

from forty.main import main
from forty.configuration import make_config


def run():
    home = environ.get("FORTY_HOME", None)
    output = environ.get("FORTY_OUTPUT", None)
    status = environ.get("FORTY_STATUS", None)

    configuration = make_config(home=home, output=output, status=status)

    options = argv[1:]
    main(options=options, configuration=configuration)


if __name__ == '__main__':
    run()
