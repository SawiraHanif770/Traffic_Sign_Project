---
title: Traffic Sign Recognition
emoji: 🚦
colorFrom: blue
colorTo: green
sdk: streamlit
app_file: main.py
pinned: false
---
🚦 Traffic Sign Recognition using CNN
An AI-powered web application that recognizes and classifies traffic signs from uploaded images using a Convolutional Neural Network (CNN) trained with TensorFlow/Keras.

Live Demo: View on Hugging Face Spaces


# Traffic_Sign_Project
Original repository credit:
deepak2233
Traffic-Signs-Recognition-using-CNN-Keras
>>>>>>> 315c951264d749dd5c4b203abe490ded6e5c3b61

We have modified and extended the original project by adding:

A Flask web interface
Unit testing (testing.py)
Threading for async prediction
Deployment on Hugging Face Spaces
API testing with Postman
Use-case diagram and flowchart

All credit for the base model and dataset goes to the original author.

📸 Demo
Upload ImagePrediction ResultUser uploads a traffic sign imageCNN returns label + confidence %

Example: Upload stop_sign.jpg → Prediction: Stop Sign (98% confidence)


✨ Features

📤 Upload any traffic sign image (JPG, PNG, JPEG)
🧠 CNN model predicts the traffic sign class automatically
📊 Shows prediction label with confidence percentage
⚠️ Handles errors gracefully (missing file, invalid format, model failure)
🔄 Threading for non-blocking prediction
✅ Unit tested with Python unittest framework
🌐 Deployed on Hugging Face Spaces (CPU-only, no GPU needed)


🛠️ Technologies Used
TechnologyPurposePythonCore programming languageTensorFlow / KerasCNN model training and inferenceFlaskBackend web frameworkHTML / CSSFrontend web interfacePostmanAPI endpoint testingunittestUnit testing of functionsthreadingConcurrent prediction executionGitHubVersion control and hostingHugging Face SpacesFree deployment platformTrelloProject management

📁 Project Structure
traffic-sign-recognition/
│
├── app.py                  # Flask backend — main application
├── testing.py              # Unit tests using unittest framework
├── best_model.h5           # Pretrained CNN model (Keras)
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Frontend web page
│
├── static/
│   └── style.css           # Styling for the web page
│
├── diagrams/
│   ├── use_case_diagram.png
│   └── flowchart.png
│
└── README.md

⚙️ How to Run Locally
1. Clone the repository
bashgit clone https://github.com/YOUR_USERNAME/traffic-sign-recognition.git
cd traffic-sign-recognition
2. Install dependencies
bashpip install -r requirements.txt
3. Run the Flask app
bashpython app.py
4. Open in browser
http://localhost:5000

🧪 Running Unit Tests
bashpython -m unittest testing.py -v
Tests included:

test_image_preprocessing — checks resize and normalize
test_model_loading — verifies best_model.h5 loads correctly
test_prediction_output — validates output label and confidence range


🔗 API Endpoint
POST /predict
Request:
Content-Type: multipart/form-data
Body: image file
Response:
json{
  "label": "Stop Sign",
  "confidence": 98.4
}
Tested using Postman — see screenshots in the report.

🧵 Threading
The prediction function runs in a separate thread to keep the web interface responsive during CNN inference:
pythonimport threading

def predict_in_thread(image, result):
    result['output'] = model.predict(image)

result = {}
t = threading.Thread(target=predict_in_thread, args=(image, result))
t.start()
t.join()

🖼️ Screenshots
LocalHost
<img width="1600" height="800" alt="p1" src="https://github.com/user-attachments/assets/47b3cd50-4180-4fe1-a579-8e45729b5785" />
<img width="1600" height="742" alt="p2" src="https://github.com/user-attachments/assets/b6744260-6df0-4cb4-a269-bb2cd5e6638f" />
Testing:
<img width="874" height="390" alt="p3" src="https://github.com/user-attachments/assets/7e0a087e-552b-4df4-ad9a-c01a366b1eeb" />
Trello-Board:
<img width="1425" height="580" alt="p5" src="https://github.com/user-attachments/assets/55df6aa3-b79f-4df0-aa93-f57b065e2788" />

Threading:
<img width="879" height="156" alt="p4" src="https://github.com/user-attachments/assets/ef073eef-6065-4eea-98a7-4c82abede0e3" />

Use-Case Diagram:
<img width="539" height="576" alt="p6" src="https://github.com/user-attachments/assets/62115385-9e75-48a7-a382-43a4d441e0ea" />

Flowchart:
<img width="477" height="773" alt="p8" src="https://github.com/user-attachments/assets/9b7aec37-8a76-4696-a273-fe1f6679d5ae" />

Hugging Face Depoyment:
<img width="1600" height="805" alt="p9" src="https://github.com/user-attachments/assets/c01fe9fa-15d5-4b7e-bcd7-4812e53484d1" />
<img width="1600" height="787" alt="p10" src="https://github.com/user-attachments/assets/960e8ff4-904e-4d68-9b99-a3cfb4405c2e" />



✅ Changes Made to Original Project
#ChangeDescription1ThreadingAdded async prediction using Python threading2Unit TestingCreated testing.py with 3 unittest test cases3Web InterfaceBuilt Flask + HTML/CSS single-page web app4API TestingTested /predict endpoint using Postman5DiagramsCreated use-case diagram and flowchart6Trello BoardManaged tasks on Trello board7DeploymentDeployed on Hugging Face Spaces8Error HandlingAdded proper error messages for invalid inputs

⚖️ Advantages & Limitations
Advantages

Fast prediction (milliseconds)
Lightweight — runs on CPU, no GPU needed
Easy to deploy and use
Clean, simple web interface

Limitations

Requires internet for Hugging Face deployment
Limited to traffic sign classes in training dataset
Accuracy may vary with poor quality images


🔮 Future Work

📱 Mobile app integration
📷 Real-time camera detection using OpenCV
🎯 Higher accuracy with larger datasets
🌍 Multi-country traffic sign support


👥 Group Members
NameRoll Number: Sawira Bibi (FA23-BSE-024) and Hadia Ajmal (FA23-BSE-046)
Course: Software Construction and Development
Semester: BSE-6
University: COMSATS University Islamabad

📄 License
This project is for educational purposes only.


