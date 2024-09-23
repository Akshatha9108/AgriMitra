import os
from flask import Flask, request, render_template, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import uuid  # To generate unique filenames

# Initialize Flask app
app = Flask(__name__)

# Path to upload folder and dataset folder
UPLOAD_FOLDER = 'PlantVillage/static/uploads/'
DATASET_FOLDER = 'C:\\Users\\aksha\\OneDrive\\Desktop\\AgriMitra\\datasets prep\\PlantVillage'  # Path to your dataset folder containing the subfolders
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your trained crop disease model
model = load_model('C:\\Users\\aksha\\OneDrive\\Desktop\\AgriMitra\\datasets prep\\PlantVillage\\crop_disease_model.keras')

# Dynamically generate class labels from the folder names in your dataset
class_labels = sorted([folder for folder in os.listdir(DATASET_FOLDER) if os.path.isdir(os.path.join(DATASET_FOLDER, folder))])

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for predicting crop disease
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Ensure the upload directory exists again (in case it's removed mid-operation)
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        # Generate a unique filename for the uploaded file
        unique_filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        file.save(filepath)

        # Load and preprocess the image
        img = load_img(filepath, target_size=(150, 150))  # Resize image to match model's input size
        img = img_to_array(img)  # Convert to numpy array
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        img = img / 255.0  # Normalize the image

        # Perform prediction
        pred = model.predict(img)
        predicted_class = class_labels[np.argmax(pred)]
        
        return render_template('index.html', prediction=predicted_class, img_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
