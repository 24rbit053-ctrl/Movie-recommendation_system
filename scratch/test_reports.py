import sys
import os
import datetime

# Add project root to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from reports import generate_pdf_report, generate_excel_report

print("Testing PDF and Excel Report Engine...")

summary_data = {
    'total_users': 45,
    'total_activities': 120,
    'total_logins': 30,
    'total_searches': 25,
    'total_movie_views': 40,
    'total_recommendations': 25,
    'active_users': 12,
    'activity_distribution': {
        'PAGE_VISIT': 45,
        'MOVIE_VIEW': 40,
        'LOGIN': 30,
        'MOVIE_SEARCH': 25,
        'RECOMMENDATION_VIEW': 25,
        'LOGOUT': 15
    },
    'top_movies': [
        {'title': 'Avatar: Fire and Ash', 'count': 28},
        {'title': 'Avengers: Doomsday', 'count': 24},
        {'title': 'The Batman - Part II', 'count': 20},
        {'title': 'Spider-Man: Beyond the Spider-Verse', 'count': 18},
        {'title': 'Dune: Messiah', 'count': 15}
    ],
    'activity_trend': [
        {'date': '2026-08-27', 'count': 12},
        {'date': '2026-08-28', 'count': 18},
        {'date': '2026-08-29', 'count': 22},
        {'date': '2026-08-30', 'count': 15},
        {'date': '2026-08-31', 'count': 30},
        {'date': '2026-09-01', 'count': 25},
        {'date': '2026-09-02', 'count': 35}
    ]
}

detailed_logs = [
    {
        'id': 1,
        'timestamp': '2026-09-02 21:00:00',
        'username': 'admin',
        'activity_type': 'LOGIN',
        'page': '/login',
        'details': 'User logged in successfully'
    },
    {
        'id': 2,
        'timestamp': '2026-09-02 21:01:15',
        'username': 'admin',
        'activity_type': 'MOVIE_SEARCH',
        'page': '/recommendations',
        'details': 'Searched similar movies for Avatar: Fire and Ash'
    },
    {
        'id': 3,
        'timestamp': '2026-09-02 21:02:30',
        'username': 'admin',
        'activity_type': 'MOVIE_VIEW',
        'page': '/movie/9001',
        'details': 'Viewed movie details for Avatar: Fire and Ash'
    }
]

user_info = {
    'username': 'admin',
    'role': 'admin',
    'created_at': '2026-08-01 10:00:00',
    'total_logins': 30,
    'last_active': '2026-09-02 21:02:30',
    'total_activities': 120
}

users_summary = [
    {
        'username': 'admin',
        'role': 'admin',
        'created_at': '2026-08-01 10:00:00',
        'login_count': 30,
        'last_active': '2026-09-02 21:02:30',
        'search_count': 25,
        'view_count': 40,
        'rec_count': 25
    }
]

try:
    pdf_buf = generate_pdf_report('overview', summary_data, detailed_logs, user_info)
    print(f"SUCCESS: PDF Report generated: {len(pdf_buf.getvalue())} bytes")

    excel_buf = generate_excel_report('overview', summary_data, detailed_logs, users_summary)
    print(f"SUCCESS: Excel Report generated: {len(excel_buf.getvalue())} bytes")
    
    print("ALL TESTS PASSED!")
except Exception as e:
    print(f"ERROR during test: {e}")
    sys.exit(1)

