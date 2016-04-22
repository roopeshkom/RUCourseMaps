from flask import Flask, request, render_template, url_for
from rucoursemaps import getLists

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':                    #when post happens
        deptnum = request.form.get('deptnum')       #get deptnum
        if deptnum == "-1":
            return render_template("404.html")
        courses,prereqs,names = getLists(deptnum)   #returns the array of 3 things
        print "\\\\\\\\\\\\\\\\\\LIST OF courses\\\\\\\\\\\\\\"
        print courses
        print "\\\\\\\\\\\\\\\\\\LIST OF prereqs\\\\\\\\\\\\\\"
        print prereqs
        print "\\\\\\\\\\\\\\\\\\LIST OF names\\\\\\\\\\\\\\\\"
        print names
        return render_template("graphs.html",courses=courses,prereqs=prereqs,names=names)
        #print stuff to debug

if __name__ == '__main__':
    app.run(debug=True)

#Special thanks to Reavor, Sakaib, AP, and Kartik
# -Bhargav Tarpara
