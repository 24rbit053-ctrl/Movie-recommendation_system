import urllib.request
import json

base = "http://127.0.0.1:5000"
genres = ["Action", "Romance", "Thriller", "Comedy", "Drama", "Sci-Fi"]

for genre in genres:
    url = base + "/api/movies/genre/" + genre
    try:
        r = urllib.request.urlopen(url)
        data = json.loads(r.read().decode())
        count = len(data.get("movies", []))
        print("PASS: /api/movies/genre/" + genre + " -> " + str(count) + " movies")
    except Exception as e:
        print("FAIL: /api/movies/genre/" + genre + " -> " + str(e))
