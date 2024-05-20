from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

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

@app.route('/result', methods=['GET'])
def result():
    name = session.get('name')
    student_number = session.get('student_number')
    gender = session.get('gender')
    major = session.get('major')
    languages = session.get('programming_languages')

    return render_template('result.html', name=name, student_number=student_number, gender=gender, major=major, languages=languages)

if __name__ == '__main__':
    app.run(debug=True)