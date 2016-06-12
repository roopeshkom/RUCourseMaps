#Imports the libraries for web scraping, json parsing, regular expressions 
from bs4 import BeautifulSoup
import urllib2
import json
import re

#Main method for getting the raw json. Takes in the subject department num, 
#and returns a list with three strings containing all the necessary data
def getLists(depnum):
	#Guards against the department number not being properly selected in the drop down
	if depnum == -1:
		return None

	#The urls of the spring and fall semster of the current year, with the selcted dep. num.
	url = "http://sis.rutgers.edu/soc/courses.json?campus=NB&semester=92016&level=U&subject="
	url2 = "http://sis.rutgers.edu/soc/courses.json?campus=NB&semester=12016&level=U&subject="
	url += str(depnum)
	url2 += str(depnum)

	#This code generates the two soup objects, and gets the string text from them
	html = urllib2.urlopen(url).read()
	html2 = urllib2.urlopen(url2).read()
	soup = BeautifulSoup(html, 'html.parser')
	soup2 = BeautifulSoup(html2, 'html.parser')
	text = soup.get_text()
	text2 = soup2.get_text()

	#This code deals with the current semster first, by parsing the retrived json
	parsed_json = json.loads(text)
	prereqs = []; courses = []; names = []
	for i in parsed_json:
		reqs = i.get('preReqNotes')
		if not (reqs is None):
			arg = str(depnum) + ":..."; added = False; already = []
			for z in re.findall(arg, str(reqs)):
				if not z in already:
					prereqs.append(z[4:7])
					prereqs.append(i.get('courseNumber'))
					added = True
				already.append(z)
			if not added:
				prereqs.append('NULL')
				prereqs.append(i.get('courseNumber'))
		else:
			prereqs.append('NULL')
			prereqs.append(i.get('courseNumber'))

		courses.append(i.get('courseNumber'))
		names.append(i.get('title'))

	#This code block does the same for the 2nd semester as the block above
	parsed_json2 = json.loads(text2)
	prereqs2 = []; courses2 = []; names2 = []
	for i in parsed_json2:
		reqs = i.get('preReqNotes')
		if not (reqs is None):
			arg = str(depnum) + ":..."; added = False; already = []
			for z in re.findall(arg, str(reqs)):
				if not z in already:
					prereqs2.append(z[4:7])
					prereqs2.append(i.get('courseNumber'))
					added = True
				already.append(z)
			if not added:
				prereqs2.append('NULL')
				prereqs2.append(i.get('courseNumber'))
		else:
			prereqs2.append('NULL')
			prereqs2.append(i.get('courseNumber'))

		courses2.append(i.get('courseNumber'))
		names2.append(i.get('title'))

	#This adds the 2nd semster courses and names
	for i in courses2:
		if not i in courses:
			courses.append(i)
	for i in names2:
		if not i in names:
			names.append(i)
	
	#This is the code that merges the two semester's courses and their prereqs together,
	#while making sure to not allow duplicates
	for i in range(0, len(prereqs2), 2):
		equal = False
		a = prereqs2[i]
		b = prereqs2[i+1]
		for j in range(0, len(prereqs), 2):
			c = prereqs[j]
			d = prereqs[j+1]
			if a+b == c+d:
					equal = True
					break
		if equal == False:
			prereqs.append(a)
			prereqs.append(b)

	#This simply generates the return list
	ret = []
	ret.append(', '.join(courses))
	ret.append(', '.join(prereqs))
	ret.append(', '.join(names))

	return ret

#Debugging method to check if program is working properly
def test():
	a, b, c = getLists(int(raw_input("Please enter the department number: ")))
	print "Classes:\n%s" % a
	print "Prereqs:\n%s" % b
	print "Names:\n%s" %c