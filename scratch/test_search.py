import urllib.request
import urllib.parse
import re
import html
import json

def test():
    query = 'The Matrix 1999 movie poster'
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/search?q={encoded_query}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            content = response.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'm="([^"]+)"', content)
            print("Raw matches found:", len(matches))
            for idx, m in enumerate(matches):
                m_decoded = html.unescape(m)
                if m_decoded.startswith('{'):
                    try:
                        js = json.loads(m_decoded)
                        print(f"Match {idx} JSON keys:", js.keys())
                        print(f"Match {idx} purl:", js.get('purl'))
                        print(f"Match {idx} murl:", js.get('murl'))
                        print(f"Match {idx} turl:", js.get('turl'))
                        print(f"Match {idx} mediaurl:", js.get('mediaurl'))
                    except Exception as e:
                        print(f"Match {idx} load failed:", e)
    except Exception as e:
        print("Failed:", e)

if __name__ == "__main__":
    test()
