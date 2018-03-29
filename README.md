# A Collection of Behave Samples

Examples of using behave.  Follows the behave official tutorial and continues with selenium examples.

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

## Plans

1. Create tests for a site that uses React.js such as: https://reactjs.org/

1. Expand behave examples from the official docs: http://behave.readthedocs.io/en/latest/

1. Expand selenium examples from the official package docs: http://selenium-python.readthedocs.io/index.html

1. Make into a python package with pipenv: https://packaging.python.org/tutorials/managing-dependencies/

1. Dockerize to allow for easier running or port to a package like this one: https://github.com/William-Yeh/docker-behave
