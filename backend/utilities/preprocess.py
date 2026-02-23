from PIL import Image
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input

def preprocess_image(image_file):
    image = Image.open(image_file).convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image)
    
    # Expand dimensions to create batch shape: (1, 224, 224, 3)
    image = np.expand_dims(image, axis=0)
    
    # Apply the exact same preprocessing used in your Kaggle notebook
    image = preprocess_input(image)
    
    return image