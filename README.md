🧬 HematoVision | Blood Cell Classification Using Transfer Learning
HematoVision is a deep learning-powered web application that classifies blood cells into four major types: Eosinophils, Lymphocytes, Monocytes, and Neutrophils. It uses transfer learning with pre-trained CNNs to deliver high accuracy and fast predictions.

🔍 Project Overview
🎯 Objective: Develop a scalable and accurate model for automated blood cell classification using Convolutional Neural Networks (CNNs) and transfer learning techniques.

🗂️ Dataset: Kaggle Blood Cell Dataset

🚀 Method: Fine-tuning CNN architectures like MobileNetV2 and VGG16

🧪 Prediction Example: Upload a cell image → Model returns cell type (e.g., "Monocyte")

📁 Project Structure
java
Copy
Edit
HematoVision/
├── app.py                 → Flask backend script  
├── Blood cell.h5         → Trained Keras model  
├── requirements.txt      → Python dependencies  
├── templates/  
│   ├── home.html         → Upload interface  
│   └── result.html       → Result display  
├── static/               → Uploaded images (temporary)  
└── README.md             → Project documentation  
💻 Setup Instructions
✅ Option A: Run Locally
Clone the repository from GitHub

Open a terminal and navigate to the project folder

Run the command: pip install -r requirements.txt

Start the app by running: python app.py

Open a browser and go to: http://localhost:5000

🛠 Option B: Run in Visual Studio Code (VS Code)
Open VS Code

Select the HematoVision folder

Open the terminal

(Optional) Create and activate a virtual environment

Run: pip install -r requirements.txt

Run the app with: python app.py

Open your browser at http://127.0.0.1:5000

🌐 Option C: Run on Google Colab
Install required packages

Upload the following files:

Blood cell.h5

home.html

result.html

app.py

Start the app with: python app.py

Use the ngrok URL to access your app

🧠 Use Case Scenarios
Application Area	Description
Diagnostic Labs		Enhances efficiency by automating blood cell analysis
Remote Consultations	Enables fast, real-time results via telemedicine platforms
Education & Training	Useful for students and lab technicians to learn and validate cell types

🧰 Tech Stack
Layer		Tools Used
Frontend	HTML, Bootstrap (optional)
Backend		Flask, Flask-ngrok
Model		TensorFlow/Keras (MobileNetV2 / VGG16 with Transfer Learning)
Hosting		Google Colab + ngrok

📦 Requirements
flask

flask-ngrok

tensorflow

numpy

Pillow

ngrok

Install them all using:
pip install -r requirements.txt


📫 Contact
Rayachoti Vamsi
📧 vamsirayachoti600@gmail.com

