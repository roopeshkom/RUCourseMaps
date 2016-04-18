README
=======
This is a tool for students of Rutgers University to see all of the courses in any partcular department by prerequsite.
Just go to [rucoursemaps.com](https://rucoursemaps.com)

This is a web flask application.
Graphs were generated via the Cytoscape API.

**Note:** Courses and prerequisites listed are based off of Rutgers University's Fall 2016 semester. Selection of different semesters / years is a planned feature that will be implemented in the near future.


**How to run local host:**
First you need to clone the repo
`git clone https://github.com/roopeshkom/RUCourseMaps.git`

Then make sure you have python 2.7 installed.
Next cd into the repo and run
`python app.py`

Finally go to brower
`localhost:5000`

**Need to publish. Please help**
--------------------------------
Feel free to fork

**TODO:**
  1. upload project to hiroku and connect domain name
  2. correct json parsing algo for all SOE departments, where it is not detecting prereqs
	-> To do this we need to integrate the Spring and Fall Semester JSON together to detect all posssible prereqs
  3. add clicking functionality such that it will highlight the nodes and previosu nodes
  4. add hover-over node -> textbox (course name and desciption)
