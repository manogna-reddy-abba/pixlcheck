# PixlCheck: AI Synthetic Image Detector 🕵️‍♂️🔍

PixlCheck is a lightweight, end-to-end deep learning web application designed to classify images as either "Real" or "AI-Generated." It utilizes a fine-tuned ResNet-50 Convolutional Neural Network (CNN) trained on the CIFAKE dataset to analyze microscopic visual artifacts and provide real-time confidence scores.

## 🚀 Tech Stack
* **Machine Learning:** TensorFlow, Keras (ResNet-50 Backbone)
* **Backend API:** Python, Flask, Flask-CORS
* **Frontend UI:** HTML5, CSS3, Vanilla JavaScript
* **Hardware Acceleration:** Native Apple Silicon support (`tensorflow-macos`, `tensorflow-metal`)

## 🧠 Model Architecture
The core inference engine is a ResNet-50 model. Instead of relying on manual feature extraction, the model utilizes deep residual learning and skip connections to identify generative inconsistencies (such as unnatural textures and background blending errors) that are invisible to the naked eye. Input images are strictly formatted to 224x224 pixels and normalized using the official ResNet50 preprocessing pipeline.

## ⚙️ Local Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
**2. Set Up the Virtual Environment
Create and activate a Python virtual environment to keep your dependencies isolated.

Bash
# Navigate to the backend directory
cd backend

# Create the virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
**3. Install Dependencies
Install the necessary Python libraries.

Bash
pip install -r requirements.txt
**4. Add the Model File
[!IMPORTANT]
Due to GitHub's file size limits, the trained model (cifake_detector_resnet50.keras) is not included in this repository.

Download the model file.

Place it inside the backend/model/ directory.

Ensure the filename matches: cifake_detector_resnet50.keras.

**5. Run the Backend API
Start the Flask server.

Bash
python3 website.py
The server should now be running at http://127.0.0.1:5000.

**6. Launch the Frontend
Since this is a Vanilla JS project, you don't need a build step.

Simply open frontend/index.html in your preferred web browser.

Or, if using VS Code, right-click index.html and select "Open with Live Server".

📂 Project Structure
Plaintext
pixlcheck/
├── backend/
│   ├── model/           # Store .keras model here
│   ├── utilities/       # Image preprocessing logic
│   ├── website.py       # Flask API Entry point
│   └── requirements.txt # Python dependencies
├── frontend/
│   ├── assets/          # Logos and UI images
│   ├── css/             # Styling
│   └── index.html       # Main UI
└── README.md
🛠️ Usage
Upload any image (JPG/PNG).

Click "Analyze Image".

View the classification result (Real vs. AI) and the confidence percentage.