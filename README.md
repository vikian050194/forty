# forty

[![MIT license][license-badge]][license-url]
[![Maintenance status][status-badge]][status-url]

## About

**forty** it a tool that can help you track (working) time, take a break and many more


## Motivation

Firstly, **forty** is a pet-project

Secondly, there are a lot of flexible and powerful time and work trackers but from my point of view all of them is too complex and I don't need a biggest part of provided features


## Requirements

Python version 3.8 or higher

Developed and tested on Ubuntu 20.04


## Installation

Rigth now the best way to install **forty** is following one:
1. Clone the repo
    ```
    git clone https://github.com/vikian050194/forty.git
    ```
2. Install the package locally

   Privileged user is required because bash completion file will be copied to `etc` directory
    ```
    pip3 install .
    ```
3. Call installed package via a generated standalone "shim" script
    ```
    forty
    ```


## Usage

**forty** supports concurrent work on different projects like work, freelance or pet-projects

There are *actions* and *commands*

But from user perspective there is no difference between this two types because it is all the same - just (different) options to invoke from the terminal

*Actions* are stored and used for calculations

*Commands* are calculations and **TODO**

### Actions

**Work**

Time is optional and it's possible to specify just `h`, `hh` or `hh:mm` - all possible subcases of full format

| Command | Description |
| --- | --- |
| `start hh:mm:ss` | Start work |
| `finish hh:mm:ss` | Finish work |

### Commands

**Help**

| Command | Description |
| --- | --- |
| `help` | Help information |
| `version` | Installed version |

**Status**

| Command | Description |
| --- | --- |
| `whatsup` | All possible information at once |
| `status` | Current status |
| `today` | Today time |
| `total` | Total time |
| `passed` | Passed time |
| `remained` | Remained time |

**History**

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

**Project-wide**

| Command | Description | Value |
| --- | --- | --- |
| `day` | Day time limit | Optional |
| `total` | Total time limit | Optional |
| `break` | Total time limit | Optional |

**Global**

| Command | Description | Value |
| --- | --- | --- |
| `break` | Day time limit | Optional |
| `concurrency` | Total time limit | Optional |

## Tests

TDD is cool and I use it here!

Module for testing is `unittest`

```
python3 -m unittest discover -t=. -s=tests/ -p=test_*.py
```

[status-url]: https://github.com/vikian050194/forty/pulse
[status-badge]: https://img.shields.io/github/last-commit/vikian050194/forty.svg

[license-url]: https://github.com/vikian050194/forty/blob/master/LICENSE
[license-badge]: https://img.shields.io/github/license/vikian050194/forty.svg
