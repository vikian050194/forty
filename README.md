# forty

[![MIT license][license-badge]][license-url]
[![Maintenance status][status-badge]][status-url]
[![Code coverage][coverage-badge]][coverage-url]

## About

**forty** is a tool that can help you track (working) time, take a break and many more

Also there is [todo list](./TODO.md).

## Motivation

There are a lot of flexible and powerful time and work trackers but as for me all of them are too complex and I don't need a biggest part of provided features

## Requirements

Python version 3.8 or higher

Developed and tested on Ubuntu 20.04

## Installation

Rigth now the best way to install **forty** is following one:
1. Clone the repo
    ```
    git clone https://github.com/vikian050194/forty.git
    ```
2. Make directory for custom bash completion scripts and grant full access for everyone (TODO: fix this dirty manual hack)
    ```
    mkdir "$HOME/.bash_completion.d"
    chmod 777 "$HOME/.bash_completion.d"
    ```
3. Install the package globally

   Privileged user is required because bash completion file will be copied to `etc` directory
    ```
    pip3 install .
    ```
4. Call installed package via a generated standalone "shim" script
    ```
    forty
    ```
    or run Python module
    ```
    python3 forty
    ```

## Development

```
virtualenv venv
source venv/bin/activate
pip install -e .
```

## Usage

**forty** supports concurrent work on different projects like work, freelance or pet-projects

In general invocation has following format `forty [COMMAND] [OPTIONS]`

### Automation

Use service to get advantage of auto-start and auto-finish

```
bash automation/setup.sh
```

To remove service

```
bash automation/clean.sh
```

### Work

Format: `forty [COMMAND] [OPTION]`

Time is optional and it's possible to specify just `h`, `hh` or `hh:mm` - all possible subcases of full format
Date is optional, but must be specified in full format `yyyy-mm-dd`

| Verb | Description |
| --- | --- |
| `start YYYY-MM-DD hh:mm:ss` | Start work |
| `finish YYYY-MM-DD hh:mm:ss` | Finish work |

**Examples**

- `forty start`
- `forty start 10`
- `forty start 10:32`
- `forty start :32`
- `forty start 10:32:45`
- `forty start ::45`
- `forty start 2022-04-28 20:45:17`

### Help

Format: `forty [COMMAND]`

| Command | Description |
| --- | --- |
| `help` | Help information |
| `version` | Installed version |

**Status**

Format: `forty status [VALUE]`

| Value | Description |
| --- | --- |
| `full` | All information |
| `only` | Current status |
| `today` | Today time |
| `total` | Total time |
| `passed` | Passed time |
| `remained` | Remained time |
| `interval` | Today you are working `from` and `to` |

**History**

Format: `forty [COMMAND] [OPTION]`

| Command | Description |
| --- | --- |
| `reset` | Remove all stored actions, clear the whole history |
| `undo n` | Undo last `n` actions, `n` is optional and default value is `1` |

### Configuration

There are three ways and layers of configuration

**Environment variables**

| Name | Description | Value |
| --- | --- | --- |
| `FORTY_HOME` | Home directory where `.forty` is stored | Any valid pathv|
| `FORTY_OUTPUT` | Output format | `human`, `plain` or `json` |
| `FORTY_STATUS` | Status type | See valid values above |

**Project-wide**

| Name | Description | Value |
| --- | --- | --- |
| `day_limit` | Day time limit | Optional |
| `total_limit` | Total time limit | Optional |
| TODO `break` | Default break duration | Optional |
| TODO `lunch` | Default lunch duration | Optional |

**Global**

TODO

| Name | Description | Value |
| --- | --- | --- |
| `break` | Default break duration | Optional |
| `lunch` | Default break duration | Optional |
| `concurrency` | Auto-stop | Optional |

## Tests

Module for testing is `unittest`

```
python3 -m unittest discover -t=. -s=tests/ -p=test_*.py
```

or

```
./shell/test.sh
```

### Coverage

Generate coverage results
```
coverage run -m unittest
```

To get total coverage percent
```
coverage report --format=total
```

To make text report
```
coverage report --format=text
```

To make HTML coverage report run following commands
```
coverage html
```

or

```
./shell/coverage.sh
```

[status-url]: https://github.com/vikian050194/forty/pulse
[status-badge]: https://img.shields.io/github/last-commit/vikian050194/forty.svg

[license-url]: https://github.com/vikian050194/forty/blob/master/LICENSE
[license-badge]: https://img.shields.io/github/license/vikian050194/forty.svg

[coverage-url]: https://codecov.io/gh/vikian050194/forty
[coverage-badge]: https://img.shields.io/codecov/c/github/vikian050194/forty
