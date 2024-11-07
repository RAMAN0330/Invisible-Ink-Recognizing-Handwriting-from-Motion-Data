# Motion-Based Handwriting Recognition

This project explores handwriting recognition using motion sensor data without relying on traditional visual input. Our model uses yaw, pitch, and roll data captured from a motion sensor-equipped pen to classify handwritten English letters, aiming for applications in VR/AR and scenarios where visual-based methods are impractical.

## Authors

- [Raman](https://github.com/RAMAN0330)
- [Roma](https://github.com/romajoshi17)
- [Aman](https://github.com/Aman-Vishwakarma1729)
- [Bhuvan](https://github.com/BhuvanKapoor)
- [Bharat](https://github.com/Sh-bharat)

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset and Features](#dataset-and-features)
3. [Data Processing](#data-processing)
4. [Methods](#methods)
5. [Experiments](#experiments)
6. [Results](#results)
7. [Conclusion and Future Work](#conclusion-and-future-work)

## Introduction

The project defines a **Invisible Ink: Recognizing Handwriting from Motion Data** where handwritten text is recognized solely based on motion data rather than visual features. Unlike OCR, which depends on images, this approach uses motion sensor data to classify individual letters written with a pen. This approach aims to address the need for digitizing handwriting in applications such as VR and AR.


## Dataset and Features

### Hardware and Data Collection
The hardware setup includes an MPU9250 9-axis motion sensor mounted on an Arduino Uno R3, paired with a stylus pen. Data was collected from 20 participants, each writing lowercase English letters, resulting in 10,400 sequences of yaw, pitch, and roll data.

### Data Format
Each data sequence captures:
- **Time delta (td)**: Time between frames
- **Yaw, Pitch, Roll**: Rotation angles in degrees
- **Ax, Ay, Az**: Acceleration on each Cartesian axis

## Data Processing

1. **Data Augmentation**: Increases dataset size by adding noise, small rotations, and stretching each sequence.
2. **Calibration & Normalization**: Adjusts each user's data to account for differences in pen-holding.
3. **Denoising Autoencoder**: Removes noise from raw sensor data, preserving descriptive features for better classification.

## Methods

### Models
We explored four different classification models:
- **K-Nearest Neighbors (KNN)**: Used as a baseline.
- **Support Vector Machine (SVM)**: Multi-class classification with a one-vs-all approach.
- **Convolutional Neural Network (CNN)**: Processes yaw, pitch, and roll as separate channels.
- **Recurrent Neural Network (RNN)**: Utilizes LSTM layers for capturing temporal data, showing the best performance.

## Experiments

### Data Splitting
Two strategies were used:
- **Random Split**: 80/10/10 train/dev/test for generalization within the same subjects.
- **Subject Split**: Train on different subjects than those in the test set, assessing model performance with unseen subjects.

### Training & Testing
- All models were tested with and without data augmentation and denoising. 
- RNN showed the best performance, especially on unseen subjects when augmented and denoised data were used.

## Results

| Model      | Random Split Accuracy | Subject Split Accuracy |
|------------|------------------------|------------------------|
| KNN        | 72.1%                 | 12.8%                 |
| SVM        | 59.1%                 | 15.6%                 |
| CNN        | 71.0%                 | 35.8%                 |
| RNN        | 77.6%                 | 40.6%                 |

RNN with data augmentation and denoising autoencoder reached the highest accuracy.

## Conclusion and Future Work

This study demonstrates that motion sensor data can be effective for handwriting recognition. Future work includes:
- Exploring uppercase alphabet recognition.
- Improving generalization with cross-validation.
- Using alternative sensors like VR controllers for better accuracy.

