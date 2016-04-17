from sys import argv
import json
import re

with open(argv[1]) as inp:
	parsed_json = json.loads(inp.read())
	prereqs = []; courses = []
	for i in parsed_json:
		courses.append(i.get('courseNumber'))
		text = i.get('preReqNotes')
		if not (text is None):
			for m in re.finditer("198:... ", str(text)):
				if not (m is None):
					prereqs.append((m.group(), "%s:%s" % (i.get('subject'), i.get('courseNumber'))))
				else:
					prereqs.append(('nothing', "%s:%s" % (i.get('subject'), i.get('courseNumber'))))
		else:
			prereqs.append(('nothing', "%s:%s" % (i.get('subject'), i.get('courseNumber'))))

	print "Courses:\n%s" % courses
	print "Prereqs:\n%s" % prereqs
