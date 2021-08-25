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
    forty help
    ```
    or just
    ```
    forty
    ```


## Usage

**Forty** support concurrent work on different projects like work, freelance or pet-projects

Project has following optional options:
- Day limit
- Total limit

There are _actions_ and _commands_

But from user perspective there is no difference between this two types because it is all the same - just (different) options to invoke from terminal

Actions are stored and used for calculations

Commands are "calculations"


### Actions

1. Start work
    ```
    forty start
    ```

2. Finish work
    ```
    forty finish
    ```


### Commands

1. Get full list of all awailable actions and commands
    ```
    forty help
    ```
    or just
    ```
    forty
    ```

2. Remove all stored actions
    ```
    forty reset
    ```

## Features

### Common
- [ ] number of working day

### Working time
- [x] total passed time
- [x] total remained time
- [x] today passed time
- [x] today remained time

### Breaks
- [ ] time passed since latest breake
- [ ] today breaks count

### Configuration
- [x] flexible configuration


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
