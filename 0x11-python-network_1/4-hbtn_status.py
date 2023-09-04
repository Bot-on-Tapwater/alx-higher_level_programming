#!/usr/bin/python3
"""Use requests to fetch url"""

if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"

    with requests.get(url) as response:
        # read content of response
        content = response.text

        # print the content
        print(f"Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
