
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


# We are defining Developer class which inherits from Employee class
#
class Developer(Employee):
	raise_amount = 1.10 # here raise_amount will be 1.10 for developer class but it will remain same 1.04 for employee class

	# We are defining init method for developer class and instaed of redefining everything in init of developer class
	# we use init of employee class and pass first, last and pay as argument as shown below
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		# Employee.__init__(self, fisrt, last, pay) # Other way of calling init of parent class(Employee in this case)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__( first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print('--->', emp.full_name())

dev1 = Developer('sheldon', 'cooper', 5000, 'c++')
dev2 = Developer('Prathamesh', 'rahate', 6000, 'Embedded C')

# To print info about class use help function as shown below
# print(help(Developer))

mgr_1 = Manager('Bradley', 'Cooper', 15000, [dev1])

print(mgr_1.email)
print(mgr_1.add_emp(dev2))
print(mgr_1.print_emp())

