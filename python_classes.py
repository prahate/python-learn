# self is defined as an instance of a class(similar to this in c++),and variables e.g. first, last and pay are called instance variables.
# instance variables are the ones that are unique for each instance e.g. first, last and pay. They are unique to each instance.
# __init__ is called as constructor(in languages like c++), this function is called as soon as we create object/instance of the class.
# we can pass default values to functions as __init__(self, pay=3000)

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def full_name(self):
		return '{} {}'.format(self.first, self.last)

# below e1 and e2 are called instances of class employee
e1 = Employee('Prath', 'rahate', 5000)
e2 = Employee('Prathamesh', 'rahate', 5000)

print(e1.full_name())
# other way to call function instaed of using  object
# print(Employee.full_name(e1))
print(e2.full_name())
