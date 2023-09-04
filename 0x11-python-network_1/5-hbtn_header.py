#!/usr/bin/python3
"""Use requests to fetch url"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    with requests.get(url) as response:
        # read content of response
        content = response.headers['X-Request-Id']

        # print the content
        print(content)
