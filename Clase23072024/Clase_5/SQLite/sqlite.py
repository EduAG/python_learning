"""
https://sentry.io/answers/delete-a-file-or-folder-in-python/ ---- delete archive for SQLITE
https://stackoverflow.com/questions/25371636/how-to-get-sqlite-result-error-codes-in-python --- try catch
https://www.ionos.com/digitalguide/websites/web-development/sqlite3-python/  ----SQLITE
"""


import sqlite3
import os
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

#print(connection.total_changes)

cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")

sql_query = "INSERT INTO example VALUES (?, ?, ?)"
sql_data = (1, 'alice', 20)

try:
    cursor.execute(sql_query, sql_data)
    connection.commit()


except sqlite3.Error as er:
    print(er.sqlite_errorcode)  # Prints 275
    print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK


cursor.execute("SELECT * FROM example")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()

os.remove('test.db')