#!/usr/bin/python3
"""Fetch from a host"""

if __name__ == '__main__':

    import urllib.request

    # url to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # response from url
    response = urllib.request.urlopen(url)

    # read content of response
    content = response.read()

    # decode content to a string
    decoded_content = content.decode("utf-8")

    # print the content
    print(f"Body response:\n\t- type: {type(content)}\
          \n\t- content: {content}\n\t- utf8 content: {decoded_content}")

    # close the response
    response.close()
