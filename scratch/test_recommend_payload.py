import urllib.request
import urllib.parse
import json
import http.cookiejar

# Create cookie jar to store session cookies
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 1. Login as admin
login_url = "http://127.0.0.1:5000/login"
login_data = urllib.parse.urlencode({
    "username": "admin",
    "password": "admin123",
    "login_type": "admin"
}).encode('utf-8')

req = urllib.request.Request(login_url, data=login_data)
try:
    with opener.open(req) as response:
        print("Login status code:", response.getcode())
except Exception as e:
    print("Login failed:", e)

# 2. Request recommendation for Inception
recommend_url = "http://127.0.0.1:5000/api/recommend"
recommend_data = json.dumps({
    "title": "Inception"
}).encode('utf-8')

req = urllib.request.Request(
    recommend_url, 
    data=recommend_data, 
    headers={'Content-Type': 'application/json'}
)

try:
    with opener.open(req) as response:
        print("Recommend status code:", response.getcode())
        data = json.loads(response.read().decode('utf-8'))
        print("Status:", data.get("status"))
        print("Target movie title:", data.get("target_movie", {}).get("title"))
        print("Recommendations count:", len(data.get("recommendations", [])))
        print("First recommendation title:", data.get("recommendations", [{}])[0].get("title"))
except Exception as e:
    print("Recommendation request failed:", e)
