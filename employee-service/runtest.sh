#!/bin/bash
# Utility script for running unit tests using pytest.
#
# Usage (same with pytest):
# sh runtests.sh tests/                                    # run entire test package
# sh runtests.sh tests/test_file.py -v                     # run single test module
# sh runtests.sh tests/test_file.py -v -k test_case_name   # run single test case
#
docker-compose build {{service_name}}-service && \
docker-compose run --rm {{service_name}}-service pytest "$@"