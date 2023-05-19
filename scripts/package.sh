#!/bin/bash

APP_DIR="TA-unifi-os"

echo "Creating ${APP_DIR}.tgz"

find . -type d -name __pycache__ -delete
COPYFILE_DISABLE=1 tar czf "${APP_DIR}.tgz" \
    --exclude '*/__pycache__/*' \
    --exclude "./scripts/*" \
    --exclude "./.github" \
    --exclude "./.git" \
    --exclude "./*.tgz" \
    ./

echo "Done!"
