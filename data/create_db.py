import sqlite3

# data/company.db bazasini yaratamiz
conn = sqlite3.connect("data/company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    year INTEGER PRIMARY KEY,
    revenue REAL,
    expenses REAL
)
""")

cursor.executemany("""
INSERT OR REPLACE INTO sales (year, revenue, expenses) VALUES (?, ?, ?)
""", [
    (2023, 300000.0, 180000.0),
    (2024, 500000.0, 250000.0),
    (2025, 750000.0, 350000.0)
])

conn.commit()
conn.close()
print("✅ SQLite baza (data/company.db) muvaffaqiyatli yaratildi!")