#!/usr/bin/env bash

set -euo pipefail

rm -f commands.sh && touch commands.sh
./main.py --year=2020 --pipe=commands.sh "$1"
cat commands.sh >> commands_total.sh