# Potato Leaf Disease Classification using Deep Learning (CNN)

## Project Overview

Plant diseases significantly impact crop yield and food security worldwide. Early and accurate disease detection can help farmers take corrective action before infections spread.

This project develops a **Convolutional Neural Network (CNN)** using **TensorFlow/Keras** to automatically classify potato leaf images into three categories:

* 🟢 Healthy
* 🟤 Early Blight
* ⚫ Late Blight

The model learns visual disease patterns directly from images and can be used as the foundation for real-world agricultural diagnostic applications.

---

## Business Problem

Manual disease diagnosis requires agricultural expertise and can be time-consuming, especially in large farming operations.

The objective of this project is to:

* Detect potato diseases from leaf images
* Reduce reliance on manual inspection
* Enable faster disease identification
* Demonstrate the application of deep learning in precision agriculture

---

## Dataset

The project uses the **PlantVillage Potato Dataset**, containing labeled images of potato leaves.

### Classes

| Class        | Description                                      |
| ------------ | ------------------------------------------------ |
| Healthy      | No disease symptoms                              |
| Early Blight | Fungal disease causing leaf damage               |
| Late Blight  | Severe disease responsible for major crop losses |

### Image Processing

All images are:

* Resized to **256 × 256**
* Converted to RGB format
* Normalized to pixel values between **0 and 1**

---

## Technical Approach

### 1. Data Pipeline

TensorFlow's `image_dataset_from_directory()` was used to:

* Load images directly from storage
* Automatically generate labels
* Batch data efficiently

Dataset split:

| Dataset    | Percentage |
| ---------- | ---------- |
| Training   | 80%        |
| Validation | 10%        |
| Test       | 10%        |

Additional optimizations:

* Caching
* Shuffling
* Prefetching

These techniques improve GPU utilization and training speed.

---

### 2. Data Augmentation

To improve model generalization and reduce overfitting, the training dataset was augmented using:

* Random horizontal flips
* Random vertical flips
* Random rotations

This exposes the model to a wider variety of leaf orientations.

---

### 3. CNN Architecture

The model consists of:

* Input preprocessing layer
* Multiple convolutional layers
* Max pooling layers
* Fully connected dense layers
* Softmax output layer

Architecture summary:

```text
Input Image (256x256x3)
        ↓
Rescaling Layer
        ↓
Conv2D (32 filters)
        ↓
MaxPooling
        ↓
Conv2D (64 filters)
        ↓
MaxPooling
        ↓
Conv2D (64 filters)
        ↓
MaxPooling
        ↓
Conv2D (64 filters)
        ↓
MaxPooling
        ↓
Conv2D (64 filters)
        ↓
MaxPooling
        ↓
Conv2D (64 filters)
        ↓
MaxPooling
        ↓
Flatten
        ↓
Dense (64)
        ↓
Dense (3, Softmax)
```

---

## Model Training

### Configuration

```python
BATCH_SIZE = 32
IMAGE_SIZE = 256
CHANNELS = 3
EPOCHS = 50
```

### Training Setup

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Metric: Accuracy

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

---

## Evaluation

The model was evaluated on a completely unseen test dataset.

```python
scores = model.evaluate(test_ds)
```

Performance was monitored through:

* Training Accuracy
* Validation Accuracy
* Training Loss
* Validation Loss

Learning curves were plotted to analyze convergence and potential overfitting.

---

## Inference Pipeline

A prediction function was created to:

1. Accept a leaf image
2. Generate class probabilities
3. Return:

   * Predicted disease
   * Confidence score

Example output:

```text
Actual: Potato___Late_blight
Predicted: Potato___Late_blight
Confidence: 98.6%
```

---

## Key Skills Demonstrated

### Deep Learning

* Convolutional Neural Networks (CNNs)
* Image Classification
* Transferable Computer Vision Concepts

### TensorFlow / Keras

* Data pipelines
* Dataset optimization
* Model training
* Model evaluation
* Model persistence

### Machine Learning Engineering

* Train/Validation/Test splitting
* Data augmentation
* Performance monitoring
* Production-ready inference functions

---

## Project Structure

```text
Potato-Disease-Classification/
│
├── Potato_Disease_Classification.ipynb
├── dataset/
│   ├── Potato___Healthy/
│   ├── Potato___Early_blight/
│   └── Potato___Late_blight/
│
├── saved_model/
│   └── Potato_Disease_Model.keras
│
├── images/
│
└── README.md
```

---

## Future Improvements

Potential enhancements include:

* Transfer Learning using

  * EfficientNet
  * ResNet
  * MobileNet
* Hyperparameter tuning
* Model explainability with Grad-CAM
* Deployment using Flask/FastAPI
* Mobile inference for field use
* Real-time disease detection from smartphone images

---

## Impact

This project demonstrates how deep learning can be applied to agriculture to automate disease detection and support faster decision-making. Beyond the specific potato dataset, the workflow can be adapted to other crops and plant diseases, making it a strong example of an end-to-end computer vision project.

### Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Google Colab

---

### Author

**Franck Fossi**

Machine Learning & Data Science Portfolio Project focused on Computer Vision, CNNs, and Agricultural AI applications.
# Potato_disease_Detection
