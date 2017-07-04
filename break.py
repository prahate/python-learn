import webbrowser
import time
count=0

while count < 4:
	print("Opening webpage at "+time.ctime())
	time.sleep(5)
	webbrowser.open('http://google.co.in')
	count= count + 1;
