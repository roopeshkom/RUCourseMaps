from flask import Flask, request, render_template, url_for
from modules.logic import getLists

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

        courses, names, prereqs = getLists(deptnum) 
        print(courses, names, prereqs, sep='\n')
        
        return render_template("graph.html", deptnum=deptnum, courses=courses, names=names, prereqs=prereqs)

@app.route('/404')
def badurl():
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)


#Special thanks to Reavan, Sakaib, AP, Kartik, and Nisarga
#Created by Alex, Roopesh, Bhargav
