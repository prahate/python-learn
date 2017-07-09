import urllib

def readText():
	fileHandle = open("/home/pratham/python-learn/movie_quotes.txt")
	fileData = fileHandle.read()
	#print(fileData)
	check_profanity(fileData)
	fileHandle.close()


def check_profanity(textToCheck):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+textToCheck)
	output = connection.read()
	#print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert")
	elif "false" in output:
		print("The document has no curse words")
	else:
		print("COuld not scan document properly")

readText()
