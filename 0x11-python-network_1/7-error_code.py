#!/usr/bin/python3
"""Handle errors in Requests"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    with requests.get(url) as response:
        if response.status_code == 200:
            print(response.text)

        elif response.status_code >= 400:
            print(f"Error code: {response.status_code}")
