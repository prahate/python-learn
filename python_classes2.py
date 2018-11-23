# self is defined as an instance of a class(similar to this in c++),and variables e.g. first, last and pay are called instance variables.
# instance variables are the ones that are unique for each instance e.g. first, last and pay. They are unique to each instance.
# __init__ is called as constructor(in languages like c++), this function is called as soon as we create object/instance of the class.
# we can pass default values to functions as __init__(self, pay=3000)

# we are going to use class variables 
# class variables are the ones that are common to instance or in other words varibales that can be shared between the instances


class Employee:

	raise_amount = 1.04 # is a class variable 

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def full_name(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		# other way to use class variables is using class name as shown below
		# self.pay = int(self.pay * Employee.raise_amount)
		# Both ways of using class variables is valid. the difference in them is
		# self.raise_amount will be valid for particular instance meaning that we can set raise_amount to different value for
		# particular instance by using e1.raise_amount = 1.05 and then if we print raise_amount for both of our instances
		# we can find that raise_amount will be 1.05 for e1 but for e2 it will still be 1.04

# below e1 and e2 are called instances of class employee
e1 = Employee('sheldon', 'cooper', 5000)
e2 = Employee('Prathamesh', 'rahate', 6000)

#illustrating use of using self.raise_amount in apply_raise method
e1.raise_amount = 1.05

print(e1.raise_amount)
print(e2.raise_amount)

e1.apply_raise()
e2.apply_raise()

print(e1.pay)
print(e2.pay)

#to print instance of class like what it contains
print(e1.__dict__)
print(e2.__dict__)
