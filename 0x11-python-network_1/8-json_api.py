#!/usr/bin/python3
"""Use requests to send a POST request"""

if __name__ == '__main__':
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"

    try:
        q = sys.argv[1]

    except IndexError:
        q = ""

    variables = {'q': q}

    with requests.post(url, data=variables) as response:
        # read content of response
        try:
            content = response.json()

            # print the content
            if len(content) != 0:
                print(f"[{content.get('id')}] {content.get('name')}")
            else:
                print("No result")

        except Exception:
            print("Not a valid JSON")
