#!/usr/bin/python3
"""Get github id"""

if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    access_token = sys.argv[2]

    url = f"https://api.github.com/users/{username}"

    headers = {"Authorization": f"token {access_token}"}

    with requests.get(url, headers=headers) as response:
        user_data = response.json()
        print(user_data.get("id"))
