import os
def rename_files():
	# 1.get the file names in folder
	fileList = os.listdir("/home/prathamesh/Documents/Dummy")
	print fileList

	#getting curent working directory for moving back
	currentDir = os.getcwd();
	print "Curent directory is "+ currentDir

	#changing the directory
	os.chdir("/home/prathamesh/Documents/Dummy");

	# 2. rename each file
	for fileName in fileList:
		os.rename(fileName, fileName.translate(None, "0123456789"))
	
	#changing back to original directory
	os.chdir(currentDir)

rename_files();
