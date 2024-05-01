from urllib import request

from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    session['name'] = request.form.get('name')
    session['student_number'] = request.form.get('student_number')
    session['gender'] = request.form.get('gender')
    session['major'] = request.form.get('major')
    session['programming_languages'] = request.form.getlist('programming_language')

    return redirect(url_for('result'))


if __name__ == '__main__':
    app.run(debug=True)