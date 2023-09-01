#!/bin/bash
# return body if status code is 200
 url=$1; if curl -sI "$url" | grep -q "200"; then curl "$url"; else echo "Bad request"; fi
