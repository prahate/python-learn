# Operator overloading in python done by using something called as maigc/dundard methods
# dundard methods are defined with '__' operators. e.g. __init__ method is also dundard method
# There are two special methods that we can define in code __repr__ and __str__
# __repr__ method will show object creation of class and it is used for debugging
# __str__ method will show string representation of employee object, it will print employee in more readable form

class Employee:
	
	raise_amount = 1.04 # are a class variables 

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@email.com'

	def full_name(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

	def __str__(self):
		return "{} - {}".format(self.full_name(), self.email)

	# we are adding dundar __add__ method for Employee class which will tell combined salary of two employees

	def __add__(self, other):
		return self.pay + other.pay

# below e1 and e2 are called instances of class employee
e1 = Employee('sheldon', 'cooper', 5000)
e2 = Employee('Prathamesh', 'rahate', 6000)

#print(e1)
#print(e2)

# other way to call repr and str methods explicitely
print(e1.__repr__())
print(e1.__str__())

# calling dundar add method on e1 and e2
print(e1 + e2)
