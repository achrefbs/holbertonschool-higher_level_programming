#!/bin/bash
#sends a JSON POST request.
curl -Xs POST -H "Content-Type: application/json" -d @"$2" "$1"
