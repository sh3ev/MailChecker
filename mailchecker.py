import re

mail = raw_input("Please enter the text: ")

if re.match("^(?!_|\.)[\w\._-]+@(?!_|\.)([\w\._-])+\.([A-Za-z]{2,3})$", mail):
	r = re.search("^(?!_|\.)[\w\._-]+@((?!_|\.)([\w\._-])+\.([A-Za-z]{2,3}))$", mail); 
	print "Domena: " + r.group(1);
	print "It's email adress !"

else:

	print "This text isn't email adress"














