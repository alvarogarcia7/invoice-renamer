#!/usr/bin/env bash

set -euo pipefail

function rename(){
  local file="$1"
  local renamer_pipe="commands.sh"
  rm -f "${renamer_pipe}" && touch "${renamer_pipe}"
  ./main.py --year=2020 --pipe="${renamer_pipe}" "${file}"
  cat "${renamer_pipe}" >> commands_total.sh
}

rename "$1"