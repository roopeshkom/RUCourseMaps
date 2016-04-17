import json
import re


def getLists(depnum):
	if depnum == -1:
		return None

	with open("testdata.txt") as inp:
		parsed_json = json.loads(inp.read())
		prereqs = []; courses = []
		for i in parsed_json:
			text = i.get('preReqNotes')
			if not (text is None):
				for m in re.findall("198:...", str(text)):
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
