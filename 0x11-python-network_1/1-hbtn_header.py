#!/usr/bin/python3
"""Display value of X-Request-Id"""

if __name__ == '__main__':
    import urllib.request
    import sys

    # url to fetch
    url = sys.argv[1]

    # response from url
    with urllib.request.urlopen(url) as response:

        # get response headers
        response_headers = dict(response.headers.items())

        # print headers
        print(response_headers.get("X-Request-Id"))
