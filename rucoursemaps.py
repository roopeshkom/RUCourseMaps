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

	for i in courses:
		i.strip('u')
	for i in prereqs:
		i.strip('u')

	ret = []
	ret.append(', '.join(courses))
	ret.append(', '.join(prereqs))
	return ret

a, b = getLists(165)
print "Classes:\n%s" % a
print "Prereqs:\n%s" % b