import sqlite3
conn = sqlite3.connect('people.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE people (
               username blob,
               password blob
               )""")

conn.commit()
conn.close()