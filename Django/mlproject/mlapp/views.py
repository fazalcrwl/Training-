from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np

# Load the model
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def index(request):
    result = None
    if request.method == 'GET' and all(param in request.GET for param in ['input1', 'input2', 'input3', 'input4']):
        try:
            # Extract inputs and convert them to integers
            input1 = int(request.GET['input1'])
            input2 = int(request.GET['input2'])
            input3 = int(request.GET['input3'])
            input4 = int(request.GET['input4'])
            
            # Prepare the input array for prediction
            inputs = np.array([[input1, input2, input3, input4]])
            prediction = model.predict(inputs)[0]
            result = f'Prediction: {prediction}'
        except ValueError:
            result = 'Invalid input. Please enter valid integers.'

    return render(request, 'index.html', {'result': result})