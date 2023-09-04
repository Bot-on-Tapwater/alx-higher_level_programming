#!/usr/bin/python3
"""Sends post request with parameters"""

if __name__ == '__main__':
        import urllib.request as request
        import urllib.parse as parse
        import sys

        url = sys.argv[1]
        email = sys.argv[2]

        variables = {'email':email}

        encoded_data = parse.urlencode(variables).encode('utf-8')

        rqst = request.Request(url, data=encoded_data, method='POST')

        with request.urlopen(rqst) as response:
                print(response.read().decode("utf-8"))
