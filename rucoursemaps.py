from bs4 import BeautifulSoup
import json
import re
import urllib2

def getLists(depnum):
	if depnum == -1:
		return None

	url = "http://sis.rutgers.edu/soc/courses.json?campus=NB&semester=92016&level=U&subject="
	url += str(depnum)

	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	text = soup.get_text()

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

	for i in courses:
		i.strip('u')
	for i in prereqs:
		i.strip('u')
	for i in names:
		i.lstrip('u')

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