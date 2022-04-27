#!/usr/bin/python3
""" Requuest user usin a letter """

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        arg = sys.argv[1]
    except Exception:
        arg = ""
    q = {"q": arg}
    req = requests.post(url, data=q)
    try:
        result = req.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
