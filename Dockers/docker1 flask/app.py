from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app=Flask(__name__)
pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)







@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    value1 = float(request.form['value1'])
    value2 = float(request.form['value2'])
    value3 = float(request.form['value3'])
    value4 =  float(request.form['value4'])
    
    # Prepare the input for the model
    input_values = np.array([[value1, value2, value3,value4]])
    
    # Predict the output
    prediction = classifier.predict(input_values)[0]
    
    return redirect(url_for('result', value1=value1, value2=value2, value3=value3, prediction=prediction))

@app.route('/result')
def result():
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    value3 = request.args.get('value3')
    prediction = request.args.get('prediction')
    return render_template('result.html', value1=value1, value2=value2, value3=value3, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)