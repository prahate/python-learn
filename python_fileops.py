# We will learn about opening and editing files from python program

# open file using open function
# other argument to open function specifies mode, r = reading, r+ = read and write, a = append to file and so on.
# The other way we can open file is to use context 
# the advantage of using context is that we don't need to close the file, it will take care of it
# f_handle = open('test.txt', 'r')
#with open('test.txt', 'r') as f_handle:
	#print(f_handle.read())
	# Instead of reading whole file contents using read we can read line by line using readlines or readline functions
	#f_contents = f_handle.readlines()
	#print(f_contents, end='')

	#f_contents = f_handle.readline()
	#print(f_contents, end='')

	#for line in f_handle:
	#	print(line, end='')

	# We are using write function to create copy of the existing file
with open('test.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)	



#	print(f_handle.name)
#	print(f_handle.mode)

# print(f_handle.read())
# f_handle.close()
