import urllib.request, urllib.error

base = "http://127.0.0.1:5000"
urls = ["/all-movies"]

for u in urls:
    try:
        r = urllib.request.urlopen(base + u)
        print("PASS: " + u + " -> " + str(r.getcode()))
    except urllib.error.HTTPError as e:
        print("FAIL: " + u + " -> HTTP " + str(e.code))
        print(e.read().decode("utf-8", errors="replace")[:2000])
    except Exception as e:
        print("ERROR: " + u + " -> " + str(e))
