#!/bin/bash
# Bash script to display the size of the body of URL response
curl -so /dev/null -w "%{http_code}" "$1"
