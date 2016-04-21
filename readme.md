README
=======
This is a tool for students of Rutgers University to see all of the courses in any particular department by prerequisite.
Just go to [rucoursemaps.com](https://rucoursemaps.com)

This is a web flask application.
Graphs were generated via the Cytoscape JS API.

**Note:** Courses and prerequisites listed are based off of Rutgers University's Fall 2016 semester. Selection of different semesters / years is a planned feature that will be implemented in the near future.


**How to run local host:**
First you need to clone the repo
`git clone https://github.com/roopeshkom/RUCourseMaps.git`

Then make sure you have python 2.7 installed, *as well as* flask.

`pip install Flask`

`pip install venv`

Next cd into the RUCourseMaps repo and run

`.\venv\Scripts\activate`

`python app.py`

then to stop the virtual environment enter `deactivate`

Finally go to browser
`localhost:5000`

**Need to publish. Please help**
--------------------------------
Feel free to fork

**TODO:**

  2. correct json parsing algo for all SOE departments, where it is not detecting prereqs
	-> To do this we need to integrate the Spring and Fall Semester JSON together to detect all posssible prereqs
  3. add clicking functionality such that it will highlight the nodes and previous nodes
  4. add hover-over node -> textbox (~~course name~~ and desciption)
 ~~ 5. Either add the course's department code into one of the strings, or create a new string that incorporates this: (Ex. 198:111, 198:112, ....). I need the department # so I can properly add href links / other fun stuff based on the specific department selected by the user.~~
