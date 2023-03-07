from flask import Flask, render_template, request, redirect
from lib import insert, select
from data import tables

app = Flask(__name__)

@app.route('/') 
def home():
    # load the home or index file
    return render_template('Trial.html')

@app.route('/interior', methods = ("GET", "POST"))
def add_interior():
    # POST request used for sending form data securely
    if request.method == "POST":
        # insert into table named interior
        insert("interior", request.form)

        return redirect('/')
    # load add form after inserting or routing
    return render_template('Interior-designing.html')

@app.route('/exterior', methods = ("GET", "POST"))
def add_exterior():
    # POST request used for sending form data securely
    if request.method == "POST":
        # insert into table named interior
        insert("exterior", request.form)

        return redirect('/')
    # load add form after inserting or routing
    return render_template('Exterior-designing.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/<name>-view')
def view(name):
    data = select(name)
    return render_template('view.html', rows = data, keys = tables[name]['keys'])

@app.route('/guide')
def guide():
    return render_template('guide_page.html')

if __name__ == "__main__":
    app.run(debug = True)