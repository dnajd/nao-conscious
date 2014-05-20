#!/bin/sh

set -eu

export PYTHONPATH=${PYTHONPATH}:src/main/python:src/test/python

if command -v nosetests >/dev/null 2>&1; then
    echo "Running tests with nose"
    nosetests -w src/test/python/subscriber_tests
else
    echo "Running tests using python unittest"
    python -m unittest subscriber_tests.test_subscribers
fi

