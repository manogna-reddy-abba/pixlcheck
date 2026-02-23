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