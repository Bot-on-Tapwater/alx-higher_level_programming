#!/usr/bin/python3
"""Fetch from a host"""

if __name__ == '__main__':
    import urllib.request

    # url to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # response from url
    with urllib.request.urlopen(url) as response:

        # read content of response
        content = response.read()

        # decode content to a string
        decoded_content = content.decode("utf-8")

        # print the content
        print(f"Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {decoded_content}")
