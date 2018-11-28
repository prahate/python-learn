# Way to add different logging levels in python program
# Python library to enable logging
import logging

# it provides four levels of logging
# DEBUG -- used for debugging or diagnosis
# INFO -- Confirmation of things working as expected
# WARNING -- Default Level. Indication of something unexpected happened but program works fine
# ERROR -- Due to serious problem software is not able to perform well
# CRITICAL -- Serious error happened, program is not able to run

# To change default logging level
#logging.basicConfig(level=logging.DEBUG)

# To write to file
#logging.basicConfig(filename='test.log', level=logging.DEBUG)

# TO add format to logging
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelno)s:%(message)s')

def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multi(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2


num1 = 20
num2 = 4


add_result = add(num1, num2)
#print("Add: {} + {} := {}". format(num1, num2, add_result))
logging.debug("Add: {} + {} := {}". format(num1, num2, add_result))

sub_result = subtract(num1, num2)
#print("Subtract: {} + {} := {}". format(num1, num2, sub_result))
logging.debug("Subtract: {} + {} := {}". format(num1, num2, sub_result))

mul_result = multi(num1, num2)
#print("Multiply: {} + {} := {}". format(num1, num2, mul_result))
logging.debug("Multiply: {} + {} := {}". format(num1, num2, mul_result))

div_result = divide(num1, num2)
#print("Subtract: {} + {} := {}". format(num1, num2, div_result))
logging.debug("Subtract: {} + {} := {}". format(num1, num2, div_result))
