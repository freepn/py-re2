#!/usr/bin/env bash

set -euxo pipefail

EXPECTED_WHEEL_COUNT=9

WHEELS="*.whl"
if [ $(echo $WHEELS | wc -w) -ne $EXPECTED_WHEEL_COUNT ]; then
    echo "Error: Expected $EXPECTED_WHEEL_COUNT wheels"
    exit 1
else
    exit 0
fi
