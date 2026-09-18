import sqlite3
import random
from datetime import datetime, timedelta

def run():
    conn = sqlite3.connect('c:/Users/Vigneshwaran M/OneDrive/New folder/OneDrive/Documents/internship project/database.db')
    cursor = conn.cursor()

    # Get some movies
    cursor.execute("SELECT movie_id, title FROM movies WHERE industry != 'Web Series' LIMIT 50")
    movies = cursor.fetchall()
    
    if not movies:
        print("No movies found. Please seed movies first.")
        return

    # Create some users
    usernames = ['alice_w', 'bob_builder', 'charlie_c', 'diana_prince', 'edward_s', 
                 'fiona_apple', 'george_lucas', 'hannah_m', 'ian_mckellen', 'julia_r']
    
    for uname in usernames:
        days = random.randint(1, 30)
        cursor.execute(f"INSERT OR IGNORE INTO users (username, password_hash, role, is_suspended, created_at) VALUES (?, ?, ?, 0, datetime('now', '-{days} days'))",
                       (uname, 'dummy_hash', 'user'))
    conn.commit()

    # Create favorites (Liked Movies)
    for _ in range(150):
        uname = random.choice(usernames)
        movie = random.choice(movies)
        try:
            cursor.execute("INSERT INTO favorites (username, movie_id) VALUES (?, ?)", (uname, movie[0]))
        except sqlite3.IntegrityError:
            pass

    # Create watchlist
    for _ in range(120):
        uname = random.choice(usernames)
        movie = random.choice(movies)
        try:
            cursor.execute("INSERT INTO watchlist (username, movie_id) VALUES (?, ?)", (uname, movie[0]))
        except sqlite3.IntegrityError:
            pass

    # Update trending movies
    cursor.execute("UPDATE movies SET is_trending = 0")
    trending_movies = random.sample(movies, 12)
    for movie in trending_movies:
        cursor.execute("UPDATE movies SET is_trending = 1 WHERE movie_id = ?", (movie[0],))

    # Add Activity Logs
    activities = []
    
    now = datetime.now()
    for _ in range(500):
        uname = random.choice(usernames)
        days_ago = random.randint(0, 30)
        hours_ago = random.randint(0, 23)
        minutes_ago = random.randint(0, 59)
        ts = (now - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)).strftime('%Y-%m-%d %H:%M:%S')
        
        act_type = random.choice(['VIEW_DETAIL', 'VIEW_DETAIL', 'SEARCH', 'SEARCH', 'LOGIN', 'PAGE_VISIT', 'RECOMMENDATION_VIEW'])
        movie = random.choice(movies)
        details = ""
        page = ""
        
        if act_type == 'VIEW_DETAIL':
            details = str(movie[0])
            page = f"/movie/{movie[0]}"
        elif act_type == 'SEARCH':
            if random.random() < 0.6:
                details = f"User searched for similar movies for {movie[1]} (ID: {movie[0]})"
                page = "/recommendations"
            else:
                details = f"Searched for: {movie[1]}"
                page = "/"
        elif act_type == 'LOGIN':
            details = "User logged in successfully"
            page = "/login"
        elif act_type == 'RECOMMENDATION_VIEW':
            details = f"Viewed recommendations for {movie[1]}"
            page = f"/recommendations/{movie[0]}"
        elif act_type == 'PAGE_VISIT':
            details = "Visited home page"
            page = "/"

        activities.append((uname, act_type, page, details, ts))

    cursor.executemany("INSERT INTO activity_logs (username, activity_type, page, details, timestamp) VALUES (?, ?, ?, ?, ?)", activities)
    
    conn.commit()
    conn.close()
    print("Database seeded with sample analytics data.")

if __name__ == '__main__':
    run()
