import sqlite3

conn = sqlite3.connect('employees2.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees3 (
#	first text,
#	last text,
#	pay integer
#	)""")


c.execute("INSERT INTO employees3 VALUES ('Sheldon', 'Cooper', '50000')")

conn.commit()

conn.close()
