#!/bin/bash
set +e
pytest --junitxml=pytest-report.xml --cov . --cov-report xml:pytest-cov.xml
set -e
#exit 0
