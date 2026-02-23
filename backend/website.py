print("🚀 website.py started")

from flask import Flask, request, jsonify
from flask_cors import CORS
from utilities.preprocess import preprocess_image
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "cifake_detector_resnet50.keras")

print("📦 Loading AI model...")
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
print("✅ AI model loaded successfully")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]

    try:
        image = preprocess_image(image_file)
        prediction = model.predict(image)[0][0]

        if prediction < 0.5:  # FAKE is 0, so less than 0.5 is AI
            result = "AI-generated"
            confidence = (1 - prediction) * 100
        else:                 # REAL is 1, so greater than 0.5 is Real
            result = "Real"
            confidence = prediction * 100

        return jsonify({
            "result": result,
            "confidence": round(float(confidence), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
