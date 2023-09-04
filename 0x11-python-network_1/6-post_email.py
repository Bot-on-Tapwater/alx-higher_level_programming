#!/usr/bin/python3
"""Use requests to send a POST request"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    variables = {'email': email}

    with requests.post(url, data=variables) as response:
        # read content of response
        content = response.text

        # print the content
        print(content)
