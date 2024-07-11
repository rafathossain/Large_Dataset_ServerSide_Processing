#!/bin/bash

echo "Deploying LDSP"
echo "========================================="
echo "Prepared by Md. Rafat Hossain"
echo "Date: 11 July 2024"
echo "Version: v1.0"
echo "========================================="

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

echo -n "Bringing up docker container..."

docker-compose -f "$SCRIPT_DIR/docker-compose.yml" down

sh "$SCRIPT_DIR/deployment/clear-junk"

sleep 1

docker-compose -f "$SCRIPT_DIR/docker-compose.yml" up -d

echo -n "Cleaning up junk..."

sh "$SCRIPT_DIR/deployment/clear-junk"

echo "COMPLETE"

echo "Deployment completed successfully."
echo "========================================="
