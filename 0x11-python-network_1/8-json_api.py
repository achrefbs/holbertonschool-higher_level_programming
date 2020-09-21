#!/usr/bin/python3
"""
a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    value = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, value)
    try:
        json_data = r.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except:
        print("Not a valid JSON")