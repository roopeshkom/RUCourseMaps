README
=======
This is a tool for students of Rutgers University to see all of the courses in any particular department by prerequisite.
Just go to [rucoursemaps.com](https://rucoursemaps.com)

This is a web flask application.
Graphs were generated via the Cytoscape JS API.

**Note:** Courses which have prereqs in other departments do not show up. This feature will be added in the future.

**How to run local host:**
First you need to clone the repo
`git clone https://github.com/roopeshkom/RUCourseMaps.git`

Then make sure you have python 2.7 installed, *as well as* flask.
cd into the RUCourseMaps repo and run

`.\venv\Scripts\activate`

Install the dependencies into the virtual environment

`pip install Flask`

`pip install venv`

Next run the app `python app.py`.

Finally go to your browser to see it at `localhost:5000`
Then to stop the virtual environment enter `deactivate`

**TODO:**
---------
  1.~~ Correct json parsing algo for all SOE departments, where it is not detecting prereqs-> To do this we need to integrate the Spring and Fall Semester JSON together to detect all possible prereqs~~
  2. Add clicking functionality such that it will highlight the nodes and previous nodes
  3. Add hover-over node function -> generates textbox (~~course name~~ and discription (in the near future feature will be added))
  4. <del>Either add the course's department code into one of the strings, or create a new string that incorporates this: (Ex. 198:111, 198:112, ....). I need the department # so I can properly add href links / other fun stuff based on the specific department selected by the user.</del>
  5. Add a feature that will add classes which have prereqs in other departments (after deployment).
  6. Change node color style (red and black)
  7. Remove semi colons in the course names
  8. Create a loading screen with cool graphics
  9. Coreqs cases
