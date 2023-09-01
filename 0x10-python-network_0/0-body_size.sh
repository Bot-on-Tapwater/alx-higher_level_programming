#!/bin/bash
# Return size (in bytes) of http response
curl -sI "$1" | grep -i "Content-Length"| cut -d " " -f 2
