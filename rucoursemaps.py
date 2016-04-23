from bs4 import BeautifulSoup
import json
import re
import urllib2

def getLists(depnum):
	if depnum == -1:
		return None

	url = "http://sis.rutgers.edu/soc/courses.json?campus=NB&semester=92016&level=U&subject="
	url2 = "http://sis.rutgers.edu/soc/courses.json?campus=NB&semester=12016&level=U&subject="
	url += str(depnum)
	url2 += str(depnum)

	html = urllib2.urlopen(url).read()
	html2 = urllib2.urlopen(url2).read()
	soup = BeautifulSoup(html, 'html.parser')
	soup2 = BeautifulSoup(html2, 'html.parser')
	text = soup.get_text()
	text2 = soup2.get_text()

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

	for i in courses:
		i.strip('u')
	for i in prereqs:
		i.strip('u')
	for i in names:
		i.lstrip('u')
	for i in courses2:
		i.strip('u')
	for i in prereqs2:
		i.strip('u')
	for i in names2:
		i.lstrip('u')

	for i in courses2:
		if not i in courses:
			courses.append(i)
	for i in names2:
		if not i in names:
			names.append(i)
	for i in xrange(0, len(prereqs2), 2):
		equal = False
		a, b = prereqs2[i], prereqs2[i+1]
		for j in xrange(0, len(prereqs), 2):
			c, d = prereqs[i], prereqs[i+1]
			if a==c and b==d:
				equal = True
				break
		if not equal:
			prereqs.append(a)
			prereqs.append(b)

	ret = []
	ret.append(', '.join(courses))
	ret.append(', '.join(prereqs))
	ret.append(', '.join(names))

	return ret

def test():
	a, b, c = getLists(int(raw_input("Please enter the department number: ")))
	print "Classes:\n%s" % a
	print "Prereqs:\n%s" % b
	print "Names:\n%s" %c