# Aquarium Species Detection using MMDetection

## Overview
This project is an object detection system built using the MMDetection framework to identify and classify various species in an aquarium environment. The system uses a pre-trained model fine-tuned on the Aquarium dataset from Roboflow, and the application can detect fish species in real time.

## Features
- **Aquarium Species Detection**: Detects and classifies different species of fish in an aquarium.
- **Model**: Utilizes a pre-trained model from MMDetection, fine-tuned for the task.
- **Real-Time Detection**: Provides real-time detection using a camera feed.
- **Mobile App**: Allows users to detect fish species using a mobile application with a camera interface.

## Dataset
The dataset used for this project is the **Aquarium Dataset** from [Roboflow](https://roboflow.com). The dataset contains images of various aquarium species, which are annotated for object detection.

## Steps to Set Up

### 1. Clone the Repository
git clone https://github.com/yourusername/aquarium-detection.git
### 2. Install Dependencies
Navigate to the project directory and install the necessary dependencies:
pip install -r requirements.txt
### 3. Setup MMDetection
Follow the installation guide from the MMDetection GitHub repository to install MMDetection and its dependencies.
### 4. Train the Model
To fine-tune the model, modify the configuration file in configs/ for the custom dataset, and run:
python tools/train.py configs/aquarium_detection.py
### 6. Inference
For real-time detection, you can run inference on images or video:
python tools/inference.py configs/aquarium_detection.py checkpoints/latest.pth --


## Important Note: Error Fix
If you encounter any errors related to array concatenation or class mismatch during training, check the following file:

Path: mmdetection/mmdet/datasets/coco.py
Modify the class definitions in this file to match the number of classes in your dataset. This adjustment may solve the issue.
