#!/bin/bash
#sends a JSON POST request.
curl -XsH POST "Content-Type: application/json" -d @"$2" "$1"
