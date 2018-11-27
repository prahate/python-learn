import sqlite3


# Creating a connection sqlite database, it will create .db file in file system
# other way to create is using memory, so database will be in memory (RAM)
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employees.db')

# To get cursor to the database
c = conn.cursor()

# Create table using cursor
#c.execute("""CREATE TABLE employees
#		(
#			first test,
#			last text,
#			pay integer
#		)""")

#c.execute("""INSERT INTO employees VALUES ('sheldon', 'cooper', '50000')""")

c.execute("SELECT * FROM employees WHERE last='cooper'")

print(c.fetchone())

# Always use conn.commit after execute statement
conn.commit()

# always good to close a connection
conn.close()
