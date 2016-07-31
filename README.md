RUCourseMaps
============
This is a tool for students of Rutgers University to see all of the courses in any particular department by prerequisite.
Just go to [rucoursemaps.com](https://rucoursemaps.com); Temporary URL [here](https://rucm.herokuapp.com/)

**Note:** Courses which have prereqs in other departments do not show up. This feature will be added in the near future.

# Setting up on localhost to help contribute
1. **PREREQS:** python2.7, and pip (`apt-get install python-pip`); Both must be reachable from the commandline
2. In a terminal cd into the folder you place your code/repositories
3. `git clone https://github.com/roopeshkom/RUCourseMaps.git`
4. `cd RUCourseMaps`
5. `sudo pip install virtualenv`
6. `virtualenv venv`  This will create a venv folder in the project repo...thats fine cause its in the gitignore
7. `. venv/bin/activate` or if your in Powershell `venv\scripts\activate`
8. `pip install -r requirements.txt`
9. ***NOTE*** before you start the local server you need to assign your local environment variable for APP_SETTINGS. Enter the command: `export APP_SETTINGS="config.DevelopmentConfig"`
To test this run `ipython` (install if you don't have it). Then `from app import app` in line 1 enter then
`print app.config` in line 2 (enter) and you should see that `DEBUG=True`
10. Finally run the local server on `python app.py`
11. Go to [localhost:5000](localhost:5000) and your done.
12. `deactivate` virtualenviroment when your done.

# TODO:
  1. Check every department and see if the prereqs are correct
  2. Add a clickable functionality such that it will highlight the node that the cursor is over and previous nodes thus making a clear path to the node
  3. Coreqs cases
  4. Prereqs in other departments
  5. Hover-over have textbox with ~~coursename~~, description and link to course page
  6. Loading screen
  7. Make it work on other browsers other than Chrome
  8. Migrate to SQLite db to help implement all the above and speed up load times
  9. Add a help for new Rutgers students page
