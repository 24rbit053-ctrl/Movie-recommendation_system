import sqlite3

conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Find Tamil / Kollywood movies
cur.execute("SELECT movie_id, title, poster_path, industry FROM movies WHERE industry='Kollywood' OR language='Tamil'")
movies = cur.fetchall()

if not movies:
    print("No Tamil/Kollywood movies found.")
else:
    for m in movies:
        print(dict(m))

conn.close()
