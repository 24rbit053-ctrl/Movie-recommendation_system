import sqlite3
conn = sqlite3.connect("database.db")
c = conn.cursor()
queries = {
    "trending_movies": "SELECT COUNT(*) FROM movies WHERE is_trending = 1 AND industry != 'Web Series'",
    "trending_series": "SELECT COUNT(*) FROM movies WHERE is_trending = 1 AND industry = 'Web Series'",
    "popular_movies": "SELECT COUNT(*) FROM movies WHERE is_popular = 1 AND industry != 'Web Series'",
    "hollywood": "SELECT COUNT(*) FROM movies WHERE industry = 'Hollywood'",
    "kollywood": "SELECT COUNT(*) FROM movies WHERE industry = 'Kollywood'",
    "web_series": "SELECT COUNT(*) FROM movies WHERE industry = 'Web Series'"
}
for name, q in queries.items():
    c.execute(q)
    print(f"{name}: {c.fetchone()[0]}")
conn.close()
