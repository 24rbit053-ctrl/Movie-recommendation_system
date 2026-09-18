import sqlite3

def dump_schema():
    conn = sqlite3.connect('c:/Users/Vigneshwaran M/OneDrive/New folder/OneDrive/Documents/internship project/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(f"Table: {table[0]}")
        print(table[1])
        print("-" * 40)
    conn.close()

if __name__ == '__main__':
    dump_schema()
