#!/bin/bash
# Bash script to display the size of the body of URL response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
