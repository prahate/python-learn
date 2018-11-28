import sqlite3
from employees import Employee

conn = sqlite3.connect('employees2.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees4 (
#	first text,
#	last text,
#	pay integer
#	)""")


def insert_employee(emp):
	with conn: 
		c.execute("INSERT INTO employees4 VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))

def get_emp_by_lastname(lastname):
	c.execute("SELECT * FROM employees4 WHERE last=?", (lastname,))
	print(c.fetchall())

def update_pay(emp, pay):
	with conn:
		emp.pay = pay
		c.execute("UPDATE employees4 SET pay=(?) WHERE first=(?) AND last=(?)", (emp.pay, emp.first, emp.last))

def delete_employee(emp):
	with conn:
		c.execute("DELETE FROM employees4 WHERE first=? AND last=?", (emp.first, emp.last))


e1 = Employee('Caroline', 'Channing', 30000)
e2 = Employee('Max', 'Black', '30000') 


# Following way of passing input to sql leads to sql injection attack
# So it is not advised to pass arguments using string formatting to sqlite
# c.execute("INSERT INTO employees3 VALUES ({}, {}, {}).format(e1.first, e1.last, e1.pay)")

insert_employee(e1)
insert_employee(e2)

# In this way we are passing arguments as tuple, if we dont want to pass any value
# We have to still pass it as tuple for example, if we only want to send first name they statement would be
# c.execute("INSERT INTO employees3 VALUES (?, ?, ?)", (e1.first,))
#c.execute("INSERT INTO employees3 VALUES (?, ?, ?)", (e1.first, e1.last, e1.pay))

# Other way to  pass values is using dictionary
#c.execute("INSERT INTO employees3 VALUES (:first, :last, :pay)", {'first':e2.first, 'last':e2.last, 'pay':e2.pay})

#c.execute("SELECT * FROM employees3 WHERE last=?", ('Dennings',))
#print(c.fetchall())

#c.execute("SELECT * FROM employees3 WHERE last=:last", {'last':'Holmes'})
#print(c.fetchall())

get_emp_by_lastname('Channing')

update_pay(e1, 40000)

delete_employee(e2)

c.execute("SELECT * FROM  employees4")
print(c.fetchall())

# Select statements doesn't need to be commited
# INSERT statemets need to be commit
conn.commit()

conn.close()
