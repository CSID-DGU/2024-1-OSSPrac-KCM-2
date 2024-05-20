from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')

def input():
    return render_template('input_info.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['University'] = request.form.get('University')
        result['Gender'] = request.form.get('gender')
        result['Major'] = request.form.get('major')
        result['Email']='@'.join(request.form.getlist('email'))
        result['Languages'] = ', '.join(request.form.getlist('languages'))
        
        return render_template('result.html',result=result)

if __name__ =='__main__':
    app.run(debug=True) 