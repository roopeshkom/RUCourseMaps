import json
import re

def getLists(depnum):
	if depnum == -1:
		return None
		
	href = "http://sis.rutgers.edu/soc/courses.json?campus=NB&semester=92016&level=U&subject="
	href += str(depnum)
	print href

	with open("testdata.txt") as inp:
		text = inp.read()
		parsed_json = json.loads(text)
		prereqs = []; courses = []
		for i in parsed_json:
			reqs = i.get('preReqNotes')
			if not (reqs is None):
				for m in re.findall("198:...", str(reqs)):
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

	ret = []
	ret.append(', '.join(courses))
	ret.append(', '.join(prereqs))
	return ret

a, b = getLists(122)
print a; print b
