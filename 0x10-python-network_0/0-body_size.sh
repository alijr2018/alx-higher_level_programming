#!/bin/bash
# cURL get body size
curl -sI "$1" | wc -c

