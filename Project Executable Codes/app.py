from flask import Flask, request, render_template, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import cv2
import os
import base64

app = Flask(__name__)

# Load the trained model
model = load_model("blood_cell.h5", compile=False)
# Define class labels
class_labels = ['Eosinophil', 'Lymphocyte', 'Monocyte', 'Neutrophil']

# Prediction function
def predict_image_class(image_path, model):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (128, 128))
    img_preprocessed = preprocess_input(img_resized.astype(np.float32).reshape((1, 128, 128, 3)))
    predictions = model.predict(img_preprocessed)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    predicted_class_label = class_labels[predicted_class_idx]
    return predicted_class_label, img_rgb

# Home + Upload Route
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files or request.files["file"].filename == "":
            return redirect(request.url)
        
        file = request.files["file"]
        filename = file.filename
        file_path = os.path.join("static", filename)
        file.save(file_path)

        predicted_class_label, img_rgb = predict_image_class(file_path, model)

        # Convert image to base64 for HTML display
        _, img_encoded = cv2.imencode('.png', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
        img_str = base64.b64encode(img_encoded).decode('utf-8')

        return render_template("result.html",
                               class_label=predicted_class_label,
                               img_data=img_str,
                               image_name=filename)
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
