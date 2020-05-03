#!/usr/bin/env bash

set -euo pipefail

function rename(){
  local file="$1"
  local renamer_pipe="commands.sh"

  ## Clearing previous to start
  rm -f "${renamer_pipe}" && touch "${renamer_pipe}"

  ## Default Year?

  # Default
  #./main.py --year=2020 --pipe="${renamer_pipe}" "${file}"

  # No Default
  ./main.py --pipe="${renamer_pipe}" "${file}"


  ## Command execution

  # Instant
  bash "${renamer_pipe}"

  # Cumulate commands
  #cat "${renamer_pipe}" >> commands_total.sh

  ## Cleanup
  rm -f "${renamer_pipe}"
}

rename "$1"
