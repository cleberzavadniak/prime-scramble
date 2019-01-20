#!/bin/sh

set -e

bin/create-prime-numbers-table.sh
bin/prepare-for-tests.sh
bin/run-tests.sh
bin/run.sh
