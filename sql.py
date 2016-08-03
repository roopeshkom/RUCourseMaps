import sqlite3
from logic import getLists


with sqlite3.connect("sample.db") as connection:
#TODO for each value of deptnum do this:
    courses,prereqs,names = getLists(198)
    courses = str(courses)
    prereqs = str(prereqs)
    names = str(names)
#TODO figure out how to get a var in the sql put
    #c = connection.cursor()
    c.execute("DROP TABLE courseData")
    c.execute("CREATE TABLE courseData(deptnum TEXT, courses TEXT, prereqs TEXT, names TEXT)")
    c.execute('INSERT INTO courseData VALUES("198", "courses", "prereqs", "names")')
