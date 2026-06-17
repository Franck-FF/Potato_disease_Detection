# 🥔 Potato Leaf Disease Classification using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![TensorFlow](https://img.shields.io/badge/TensorFlow-CNN-orange)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)]()
[![Computer Vision](https://img.shields.io/badge/Computer%20Vision-Image%20Classification-green)]()

## Live Demo

🚀 **Try the application:** [https://potatodiseasedetection-shhnbmxunxve2kftjqdwzn.streamlit.app/]

---

# Project Overview

Plant diseases can significantly reduce crop yield and food quality, creating major economic losses for farmers worldwide. Early detection is critical but often requires manual inspection and agricultural expertise.

This project uses a Convolutional Neural Network (CNN) built with TensorFlow and Keras to automatically classify potato leaf images into three categories:

* Healthy
* Early Blight
* Late Blight

The trained model has been deployed as an interactive Streamlit web application, allowing users to upload leaf images and receive instant disease predictions.

---

# Business Problem

Farmers and agricultural specialists need a fast and scalable way to identify plant diseases before they spread across crops.

Manual diagnosis can be:

* Time-consuming
* Subjective
* Difficult to scale

The goal of this project is to demonstrate how Deep Learning and Computer Vision can automate disease detection and support faster agricultural decision-making.

---

# Dataset

This project uses the PlantVillage Potato Leaf Dataset.

### Classes

| Class        | Description                                           |
| ------------ | ----------------------------------------------------- |
| Healthy      | No visible disease symptoms                           |
| Early Blight | Fungal disease affecting potato plants                |
| Late Blight  | Highly destructive disease causing severe crop losses |

### Image Characteristics

* RGB Images
* Resized to 256 × 256 pixels
* Normalized before training

---

# Solution Approach

## Data Pipeline

TensorFlow's image data pipeline was used to:

* Load images efficiently
* Automatically generate labels
* Create batches for training
* Optimize performance through caching and prefetching

Dataset split:

| Dataset    | Percentage |
| ---------- | ---------- |
| Training   | 80%        |
| Validation | 10%        |
| Test       | 10%        |

---

## Data Augmentation

To improve generalization and reduce overfitting, the following augmentation techniques were applied:

* Random horizontal flips
* Random vertical flips
* Random rotations

This helps the model learn robust disease patterns regardless of image orientation.

---

## CNN Architecture

The model consists of:

* Image preprocessing layer
* Multiple convolutional layers
* MaxPooling layers
* Dense layers
* Softmax output layer

Architecture flow:

Input Image

↓

Rescaling

↓

Conv2D + ReLU

↓

MaxPooling

↓

Conv2D + ReLU

↓

MaxPooling

↓

Conv2D + ReLU

↓

MaxPooling

↓

Dense Layers

↓

Softmax Output (3 Classes)

The network learns hierarchical visual features such as:

* Leaf texture
* Disease spots
* Color variations
* Damage patterns

---

# Model Training

### Frameworks

* TensorFlow
* Keras

### Training Configuration

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Evaluation Metric: Accuracy
* Epochs: 50
* Batch Size: 32

The model was trained on augmented images and evaluated on a separate unseen test set.

---

# Model Evaluation

The model's performance was monitored using:

* Training Accuracy
* Validation Accuracy
* Training Loss
* Validation Loss

Learning curves were analyzed throughout training to monitor convergence and identify potential overfitting.

---

# Deployment

The trained CNN model was deployed using Streamlit to create a user-friendly web application.

### Application Features

✅ Upload potato leaf images

✅ Real-time disease prediction

✅ Confidence score display

✅ Accessible through any web browser

✅ No coding knowledge required

### Deployment Stack

* TensorFlow / Keras
* Streamlit
* Python
* Streamlit Community Cloud

This deployment demonstrates the ability to move a machine learning model from experimentation to a production-facing application.

---

# Example Workflow

1. User uploads a potato leaf image
2. Application preprocesses the image
3. CNN model generates prediction probabilities
4. Predicted disease class is returned
5. Confidence score is displayed

Example:

Prediction: Late Blight

Confidence: 98.6%

---

# Project Structure

```text
Potato-Disease-Classification/
│
├── app.py
├── Potato_Disease_Classification.ipynb
├── requirements.txt
├── saved_model/
│   └── Potato_Disease_Model.keras
│
├── dataset/
│   ├── Potato___Healthy/
│   ├── Potato___Early_blight/
│   └── Potato___Late_blight/
│
├── images/
│
└── README.md
```

# Skills Demonstrated

### Machine Learning

* Supervised Learning
* Multi-Class Classification
* Model Evaluation

### Deep Learning

* Convolutional Neural Networks (CNNs)
* Image Classification
* Data Augmentation

### Machine Learning Engineering

* Data Pipelines
* Model Serialization
* Performance Optimization
* Deployment Workflows

### Tools & Technologies

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Google Colab
* Streamlit
* GitHub

---

# Future Improvements

Potential enhancements include:

* Transfer Learning with EfficientNet or ResNet
* Hyperparameter Optimization
* Grad-CAM Explainability
* Mobile Deployment
* Real-Time Camera Predictions
* Support for Additional Crop Diseases

---

# Impact

This project demonstrates an end-to-end Machine Learning workflow:

* Data Collection and Preparation
* Computer Vision Modeling
* CNN Training and Evaluation
* Model Saving and Versioning
* Web Application Deployment

By deploying the model through Streamlit, the solution becomes accessible to non-technical users and showcases the practical application of AI in agriculture.

The project highlights skills in Deep Learning, Computer Vision, TensorFlow, Model Deployment, and production-oriented Machine Learning development.

---

# Author

## Franck Fossi

### Connect With Me

* LinkedIn: [https://www.linkedin.com/in/franck-fossi-538704248/]
* GitHub: [https://github.com/dashboard]
