from flask import Flask, request, render_template
import pandas as pd
import pickle
from housing_price.pipeline.stage_04_predict import PredictPipeline
app = Flask(__name__)

model=PredictPipeline()

@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' has the form

@app.route('/predict', methods=['POST'])
def predict():
    # Collect the form data
    features = {
        'bedrooms': request.form['bedrooms'],
        'bathrooms': request.form['bathrooms'],
        'sqft_living': request.form['sqft_living'],
        'sqft_lot': request.form['sqft_lot'],
        'floors': request.form['floors'],
        'waterfront': request.form['waterfront'],
        'view': request.form['view'],
        'condition': request.form['condition'],
        'grade': request.form['grade'],
        'sqft_above': request.form['sqft_above'],
        'sqft_basement': request.form['sqft_basement'],
        'yr_built': request.form['yr_built'],
        'yr_renovated': request.form['yr_renovated'],
        'zipcode': request.form['zipcode'],
        'lat': request.form['lat'],
        'long': request.form['long'],
        'sqft_living15': request.form['sqft_living15'],
        'sqft_lot15': request.form['sqft_lot15']
    }

    # Convert to a DataFrame
    df = pd.DataFrame([features])

    # Predict using the model
    prediction = model.main(df)

    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)