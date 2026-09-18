import sqlite3

conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Check distinct industry values
cur.execute("SELECT DISTINCT industry, COUNT(*) as cnt FROM movies GROUP BY industry ORDER BY cnt DESC")
rows = cur.fetchall()
print("=== Industry values in DB ===")
for r in rows:
    print(dict(r))

conn.close()
