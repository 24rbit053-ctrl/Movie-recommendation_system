import sqlite3
import os

db_path = os.path.join(
    r'C:\Users\Vigneshwaran M\OneDrive\New folder\OneDrive\Documents\internship project',
    'database.db'
)
posters_dir = os.path.join(
    r'C:\Users\Vigneshwaran M\OneDrive\New folder\OneDrive\Documents\internship project',
    'static', 'images', 'posters'
)

conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Get all Kollywood movies
cur.execute("SELECT movie_id, title, poster_path FROM movies WHERE industry='Kollywood'")
movies = cur.fetchall()

fixed = 0
for movie in movies:
    poster_path = movie['poster_path']
    movie_id = movie['movie_id']
    title = movie['title']

    # Only fix local file paths (not http URLs)
    if poster_path and poster_path.startswith('/static/'):
        # Build actual filesystem path
        rel = poster_path.replace('/static/', '')
        full_path = os.path.join(
            r'C:\Users\Vigneshwaran M\OneDrive\New folder\OneDrive\Documents\internship project',
            'static', rel.replace('/', os.sep)
        )
        if not os.path.exists(full_path):
            # File doesn't exist — set to default
            cur.execute(
                "UPDATE movies SET poster_path = ? WHERE movie_id = ?",
                ('/static/images/posters/default.jpg', movie_id)
            )
            print(f"Fixed (missing file): [{movie_id}] {title} -> default.jpg")
            fixed += 1
        else:
            print(f"OK (file exists): [{movie_id}] {title}")

conn.commit()
conn.close()
print(f"\nDone. {fixed} Tamil movie poster paths fixed.")
