#!/usr/bin/python3
"""Manage exceptions"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    # url to fetch
    url = sys.argv[1]

    # response from url
    try:
        with urllib.request.urlopen(url) as response:

            # get response headers
            print(response.read().decode("utf-8"))

    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
