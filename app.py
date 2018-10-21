from flask import Flask, request, render_template, url_for
from bs4 import BeautifulSoup
from modules.logic import getLists
import json
import re
import urllib.request as urllib2
import os


app = Flask(__name__)

@app.route('/', methods=['GET']) 
def index():
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/graph', methods=['POST'])
def graph():
    if request.method == 'POST':                    
        deptnum = request.form.get('deptnum')      
        if deptnum == "-1":
            return render_template("404.html")
        courses,prereqs,names = getLists(deptnum) 
        print("\\\\\\\\\\\\\\\\\\LIST OF COURSES\\\\\\\\\\\\\\")
        print(courses)
        print("\\\\\\\\\\\\\\\\\\LIST OF PREREQS\\\\\\\\\\\\\\")
        print(prereqs)
        print("\\\\\\\\\\\\\\\\\\LIST OF NAMES\\\\\\\\\\\\\\\\")
        print(names)
        
        return render_template("graph.html", deptnum=deptnum, courses=courses, names=names, prereqs=prereqs)

@app.route('/404')
def badurl():
    return render_template("404.html")




if __name__ == '__main__':
    app.run(debug=True)


#Special thanks to Reavan, Sakaib, AP, Kartik, and Nisarga
#Created by Alex, Roopesh, Bhargav
