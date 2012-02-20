def progress():
	marks = experience
	spaces =  10 - experience
	loader = "[" + ("=" * int(marks)) + (" " * int(spaces)) + "]" 
	print ("Experience"+loader)
	print (loader)
	

experience = 10
progress()