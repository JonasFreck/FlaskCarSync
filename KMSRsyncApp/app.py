from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)

# List of available rsync destinations
destinations = [
    "dest1/directory/",
    "dest2/directory/",
    "dest3/directory/"
]

# environmental vars
os.environ["dest"] = destinations[0]
os.environ["source"] = "./source/directory/"

# Variable to hold the current destination
current_destination = destinations[0]



@app.route('/')
def index():
    return render_template('index.html', destinations=destinations, current_destination=current_destination)

@app.route('/change_destination', methods=['POST'])
def change_destination():
    global current_destination
    new_destination = request.form.get('destination')
    if new_destination in destinations:
        current_destination = new_destination
        os.environ["dest"] = new_destination
        print(os.environ["dest"])
        subprocess.run(['python', 'carSync.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

