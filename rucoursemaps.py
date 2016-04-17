from sys import argv
import json
import re

with open(argv[1]) as inp:
	parsed_json = json.loads(inp.read())
	classes = []; prereqs = {}
	for i in parsed_json:
		classes.append(i.get('title'))
		text = i.get('preReqNotes')
		#print "TEXT: {}".format(text)
		if not (text is None):
			m = re.search("198:... ", str(text))
			if not (m is None):
				#Currently get only the first prereq, will change to print all of them
				print m.group(0)
			else:
				print "None"
		else:
			print "None"
		

	#(i.get('title'), i.get('subject'), i.get('courseNumber'), i.get('preReqNotes'))
