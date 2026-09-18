import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from app import app

print("Testing Flask app endpoints...")

client = app.test_client()

# 1. Test public homepage
res = client.get('/')
print(f"GET / -> Status {res.status_code}")

# 2. Simulate Admin Session
with client.session_transaction() as sess:
    sess['username'] = 'admin'
    sess['role'] = 'admin'

# 3. Test Admin Console
res = client.get('/admin')
print(f"GET /admin -> Status {res.status_code}")

# 4. Test Reports Summary API (Daily, Weekly, Monthly, All)
for period in ['all', 'daily', 'weekly', 'monthly']:
    res = client.get(f'/api/admin/reports/summary?period={period}')
    print(f"GET /api/admin/reports/summary?period={period} -> Status {res.status_code}")
    assert res.status_code == 200, f"Expected 200 for {period}"

# 5. Test User Activity Audit API
res = client.get('/api/admin/reports/user/admin')
print(f"GET /api/admin/reports/user/admin -> Status {res.status_code}")
assert res.status_code == 200

# 6. Test PDF Export Endpoint
res = client.get('/admin/export/pdf?report_type=overview')
print(f"GET /admin/export/pdf?report_type=overview -> Status {res.status_code}, Content-Type: {res.content_type}")
assert res.status_code == 200
assert 'application/pdf' in res.content_type

# 7. Test Excel Export Endpoint
res = client.get('/admin/export/excel?report_type=overview')
print(f"GET /admin/export/excel?report_type=overview -> Status {res.status_code}, Content-Type: {res.content_type}")
assert res.status_code == 200

print("ALL FLASK ROUTE TESTS PASSED SUCCESSFULLY!")
