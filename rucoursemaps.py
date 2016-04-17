from bs4 import BeautifulSoup
import json
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print soup.prettify()


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
