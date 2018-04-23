# A Collection of Behave Samples

Examples of using behave.  Follows the behave official tutorial and continues with selenium examples.  Basic tests are complete that cover account management on react site codecademy.com.

This package will use Python 3, but behave supports both Python 2 and 3.

## Installation

This project is not yet packaged.  Install the following packages before attempting to run:

* behave - $ pip3 install behave

* selenium - $ pips3 install selenium

* firefox

* geckodriver from https://github.com/mozilla/geckodriver/releases, ensure it is in your PATH

* chrome

* ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/, ensure it is in your PATH

## Running

From the root of the project, you can run all tests in the suite with:

    $ behave

If large numbers of tests are failing, run it with `--stop` to stop at the first failure.

## Plans and Room for Improvement

1. Expand behave examples from the official docs: http://behave.readthedocs.io/en/latest/

1. Expand selenium examples from the bindings docs: http://selenium-python.readthedocs.io/index.html

1. Make into a python package with pipenv: https://packaging.python.org/tutorials/managing-dependencies/

1. Allow to run remotely or headlessly

1. Dockerize to allow for easier runs/port to a package like this one: https://github.com/William-Yeh/docker-behave

1. Add cross-platform capabilities using fixtures and command-line tags without duplicating features.