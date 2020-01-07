#!/bin/bash
# Bash script to display the size of the body of URL response
curl -sI "$1" | grep "Content-Length: " | cut -f 2 -d " "
