import sqlite3

conn = sqlite3.connect('base.db')
conn.row_factory = sqlite3.Row
query = """CREATE TABLE IF NOT EXISTS test(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                start DATETIME DEFAULT CURRENT_TIMESTAMP,
                end DATETIME DEFAULT NULL
            )"""
conn.execute(query)
# cur = conn.cursor()

# while True:
#     name = input("Enter the name: ")
#     query = """
#             INSERT INTO test(name) VALUES(:name)
#             """
#     cur.execute(query,{"name":name})
#     conti = input('Add more?(y/n)')
#     if conti == 'n':
#         break

# conn.commit()

tests = conn.execute("SELECT MAX(id) FROM test").fetchone()
for test in tests:
    print(int(test) +1 )
    