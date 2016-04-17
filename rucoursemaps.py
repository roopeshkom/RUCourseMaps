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
	prereqs = []; courses = []
	for i in parsed_json:
		reqs = i.get('preReqNotes')
		if not (reqs is None):
			for m in re.findall(str(depnum)+":...", str(reqs)):
				if not (m is None):
					prereqs.append(m[4:7])
				else:
					prereqs.append('NULL')
				prereqs.append(i.get('courseNumber'))
		else:
			prereqs.append('NULL')
			prereqs.append(i.get('courseNumber'))

		courses.append(i.get('courseNumber'))

	for i in courses:
		i.strip('u')
	for i in prereqs:
		i.strip('u')
	print courses
	print prereqs
	ret = []
	ret.append(', '.join(courses))
	ret.append(', '.join(prereqs))
	return ret
