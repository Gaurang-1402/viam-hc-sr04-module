#!/usr/bin/env bash
# setup.sh -- environment bootstrapper for python virtualenv

set -euo pipefail

SUDO=sudo
if ! command -v $SUDO; then
    echo no sudo on this system, proceeding as current user
    SUDO=""
fi

# Install python3-venv and python3-rpi.gpio
if command -v apt-get; then
    if dpkg -l python3-venv && dpkg -l python3-rpi.gpio; then
        echo "python3-venv and python3-rpi.gpio are installed, skipping setup"
    else
        if ! apt info python3-venv || ! apt info python3-rpi.gpio; then
            echo package info not found, trying apt update
            $SUDO apt-get -qq update
        fi
        $SUDO apt-get install -qqy python3-venv python3-rpi.gpio
    fi
else
    echo Skipping tool installation because your platform is missing apt-get.
    echo If you see failures below, install the equivalent of python3-venv and python3-rpi.gpio for your system.
fi

source .env
echo creating virtualenv at $VIRTUAL_ENV
python3 -m venv $VIRTUAL_ENV
echo installing dependencies from requirements.txt
$VIRTUAL_ENV/bin/pip install -r requirements.txt
