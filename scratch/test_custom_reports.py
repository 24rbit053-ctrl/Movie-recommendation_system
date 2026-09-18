import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from app import app

print("Testing Custom Date Reports & Dashboard APIs...")

client = app.test_client()

with client.session_transaction() as sess:
    sess['username'] = 'admin'
    sess['role'] = 'admin'

# 1. Test Custom Date Summary Endpoint
res = client.get('/api/admin/reports/summary?period=custom&start_date=2026-08-01&end_date=2026-09-02')
print(f"GET /api/admin/reports/summary?period=custom -> Status {res.status_code}")
assert res.status_code == 200
data = res.get_json()
assert data['status'] == 'success'
summary = data['summary']

print("Summary Keys Check:")
print(f" - Total Movies: {summary.get('total_movies')}")
print(f" - Total Users: {summary.get('total_users')}")
print(f" - Total Searches: {summary.get('total_searches')}")
print(f" - Total Watchlist: {summary.get('total_watchlist')}")
print(f" - Total Favourites: {summary.get('total_favourites')}")
print(f" - Total Trending: {summary.get('total_trending')}")
print(f" - Total Views: {summary.get('total_views')}")

# 2. Test Custom Date PDF Export
res_pdf = client.get('/admin/export/pdf?report_type=custom&start_date=2026-08-01&end_date=2026-09-02')
print(f"GET /admin/export/pdf?report_type=custom -> Status {res_pdf.status_code}, Length: {len(res_pdf.data)} bytes")
assert res_pdf.status_code == 200
assert 'application/pdf' in res_pdf.content_type

# 3. Test Custom Date Excel Export
res_excel = client.get('/admin/export/excel?report_type=custom&start_date=2026-08-01&end_date=2026-09-02')
print(f"GET /admin/export/excel?report_type=custom -> Status {res_excel.status_code}, Length: {len(res_excel.data)} bytes")
assert res_excel.status_code == 200

print("ALL CUSTOM DATE REPORT TESTS PASSED SUCCESSFULLY!")
