import urllib.request
import urllib.parse
import json

base_url = "http://127.0.0.1:5000"

endpoints = [
    "/",
    "/home",
    "/about",
    "/all-movies",
    "/recommendations",
    "/api/announcements",
    "/login",
    "/register"
]

for ep in endpoints:
    url = base_url + ep
    try:
        req = urllib.request.Request(url)
        # add a dummy user agent
        req.add_header('User-Agent', 'Mozilla/5.0')
        response = urllib.request.urlopen(req)
        print(f"PASS: {ep} - Status: {response.getcode()}")
    except urllib.error.HTTPError as e:
        print(f"FAIL: {ep} - Status: {e.code}")
    except Exception as e:
        print(f"ERROR: {ep} - {e}")
