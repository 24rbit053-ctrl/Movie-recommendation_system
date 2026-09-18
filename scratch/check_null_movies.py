import sqlite3

conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("SELECT COUNT(*) as cnt FROM movies WHERE genres IS NULL OR genres = ''")
row = cur.fetchone()
print("Movies with NULL/empty genres:", row['cnt'])

cur.execute("SELECT movie_id, title, genres, overview FROM movies WHERE genres IS NULL OR genres = '' LIMIT 5")
for r in cur.fetchall():
    print(dict(r))

cur.execute("SELECT COUNT(*) as cnt FROM movies WHERE overview IS NULL OR overview = ''")
row2 = cur.fetchone()
print("Movies with NULL/empty overview:", row2['cnt'])

cur.execute("SELECT COUNT(*) as cnt FROM movies WHERE vote_average IS NULL")
row3 = cur.fetchone()
print("Movies with NULL vote_average:", row3['cnt'])

conn.close()
