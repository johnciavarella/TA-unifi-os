#!/bin/bash

APP_PACKAGE="TA-unifi-os"

echo "Creating ${APP_PACKAGE}.tgz"

TEMPORARY_DIR=$(mktemp -d)
APP_PACKAGE_TEMP="${TEMPORARY_DIR}/${APP_PACKAGE}"

echo "Copying files to temp dir for packaging..."
rm -rf
mkdir -p "${APP_PACKAGE_TEMP}"
rsync -a --exclude '*/__pycache__/*' \
    --exclude "scripts/" \
    --exclude ".github" \
    --exclude ".git*" \
    --exclude "*.tgz" \
    . "${APP_PACKAGE_TEMP}"

echo "Creating ${APP_PACKAGE}.tgz"
COPYFILE_DISABLE=1 tar czf "./${APP_PACKAGE}.tgz" \
    -C "${TEMPORARY_DIR}" \
    --exclude '*/__pycache__/*' \
    --exclude "scripts/" \
    --exclude ".github" \
    --exclude ".git*" \
    --exclude "*.tgz" \
    "${APP_PACKAGE}"

echo "Done, listing files"
tar tzvf "${APP_PACKAGE}.tgz"

rm -rf "${TEMPORARY_DIR}"
