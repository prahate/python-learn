# There are two types of methods that can be deffined in python classes apart from regular methods
# classmethods and staticmethods
#
# Regular methods by default take instance of class as an argument.
#
# In classmethods we can pass class as an argument instead of an instance of the class.
# Classmethod should be used when we want particular class attribute to be changed globally meaning across the class,
# as is the case with set_raise_amount method.
#
# staticmethods are methods that do not operate on any of the class instance variables or class variables but are required in class
# 

class Employee:
	
	num_of_emps = 0	
	raise_amount = 1.04 # are a class variables 

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		
		Employee.num_of_emps += 1 # Refer to apply_raise method for explanation

	def full_name(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# we are defining classmethod called set_raise_amount, to define any regular method as classmethod
	# we have to use '@classmethod' decorator. First argument is class and second one is amount
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	# We are defining static methods to find if day is work day or not.
	# this method does not use anything from class instance
	
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

# following statement shows using classmethod
Employee.set_raise_amount(1.05)

# below e1 and e2 are called instances of class employee
e1 = Employee('sheldon', 'cooper', 5000)
e2 = Employee('Prathamesh', 'rahate', 6000)

e1.apply_raise()
e2.apply_raise()

print(e1.pay)
print(e2.pay)

import datetime
mydate = datetime.date(2018, 12, 29)
print(Employee.is_workday(mydate))

