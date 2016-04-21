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
cd into the RUCourseMaps repo and run
`.\venv\Scripts\activate`
Install the dependecies into the virtual enviroment
`pip install Flask`
`pip install venv`
Next run the app
`python app.py`
and go to your browser to see it `localhost:5000`
Then to stop the virtual environment enter `deactivate`

**Need to publish. Please help**
--------------------------------
Feel free to fork

**TODO:**

  1. Correct json parsing algo for all SOE departments, where it is not detecting prereqs
	-> To do this we need to integrate the Spring and Fall Semester JSON together to detect all posssible prereqs
  2. Add clicking functionality such that it will highlight the nodes and previous nodes
  3. Add hover-over node function -> generates textbox (~~course name~~ and desciption(in the near future feature will be added))
  4. <del>Either add the course's department code into one of the strings, or create a new string that incorporates this: (Ex. 198:111, 198:112, ....). I need the department # so I can properly add href links / other fun stuff based on the specific department selected by the user.</del>
