#!/usr/bin/python3
"""
Write a Python script that takes in a URL and
and email, sends a POST request to the passed URL
with the email as a parameter, and displays the body
of the response (decoded utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('UTF-8'))
