from flask import Flask, request, render_template, url_for
from bs4 import BeautifulSoup
from logic import getLists
import json
import re
import urllib2
import os


app = Flask(__name__)
#config
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':                    #when post happens
        deptnum = request.form.get('deptnum')       #get deptnum
        if deptnum == "-1":
            return render_template("404.html")
        courses,prereqs,names = getLists(deptnum)   #returns the array of 3 things
        print "\\\\\\\\\\\\\\\\\\LIST OF COURSES\\\\\\\\\\\\\\"
        print courses
        print "\\\\\\\\\\\\\\\\\\LIST OF PREREQS\\\\\\\\\\\\\\"
        print prereqs
        print "\\\\\\\\\\\\\\\\\\LIST OF NAMES\\\\\\\\\\\\\\\\"
        print names
        return render_template("graphs.html",courses=courses,prereqs=prereqs,names=names,deptnum=deptnum)

@app.route('/graphs', methods=['GET'])
def graphs():
    return render_template("404.html")

@app.route('/404')
def badurl():
    return render_template("404.html")

@app.route('/resources', methods=['GET'])
def resources():
    return render_template("resources.html")


if __name__ == '__main__':
    app.run()


#Special thanks to Reavan, Sakaib, AP, Kartik, and Nisarga
#Created by Alex, Roopesh, Bhargav
