# Enhancing AI-Human Interaction: Introducing the Eye Contact Recognition Model

## Background:

Nowadays, we use voice commands like “Hey Siri” to talk to machines. But these chats can feel a bit odd because they're missing the natural way people talk to each other. When we talk to people, we don't just use words; we also use our eyes and body language.

## The Problem:

Most smart machines today can't understand when someone is looking at them. Eye contact is a big part of how we communicate without speaking. We look at each other to show we're interested or ready to talk. By not noticing when someone looks at them, machines miss a big chance to chat in a more friendly way.

## Objective and Solution:

This project introduces an innovative approach to AI-human interactions. I've developed a human attention detector leveraging a binary image classifier built on the VGG16 architecture. This model is adept at detecting whether an individual is making eye contact with the device.

- **Architecture:** Utilizing VGG16, a robust architecture in computer vision, for transfer learning.
- **Extensive Training:** The model underwent 500 epochs of training on diverse datasets featuring various head poses and gaze directions.
- **Enhanced Accuracy:** Implementation of regression techniques (eventually used mediapipe for best accuracy) for precise localization of the eye area, achieving 83% validation accuracy.

## Datasets

This project leverages the extensive **Columbia Gaze Data Set**, currently one of the largest publicly available gaze datasets.

![Dataset1](images/dataset1.png)

### Detailed Statistics

- **Number of Images**: 5,880
- **Number of Subjects**: 56 (32 male, 24 female)
- **Ethnic Diversity**: 21 Asian, 19 White, 8 South Asian, 7 Black, 4 Hispanic or Latino
- **Age Range**: 18 - 36 years
- **Subjects with Glasses**: 21
- **Image Resolution**: 5,184 x 3,456 pixels

Each subject is captured in various combinations of five horizontal head poses (0°, ±15°, ±30°) and seven horizontal (0°, ±5°, ±10°, ±15°) plus three vertical gaze directions (0°, ±10°). The dataset includes a specific focus on 'gaze locking' images for each subject across different head poses.

![Dataset](images/dataset.png)

## Solution & Results

### Data Augmentation and Preparation

I use the `ImageDataGenerator` class from Keras for preparing the training and validation datasets. The configuration is as follows:

### Model Architecture

The model utilizes the VGG16 architecture with the following additional layers:

- `GlobalMaxPooling2D`
- `Dense` layer with 2048 neurons, activation='relu'
- `Dense` layer with 1 neuron, activation='sigmoid'

The model is compiled with the following settings:

- Loss Function: Binary Crossentropy
- Optimizer: RMSprop with a learning rate of 1e-6
- Metrics: Accuracy

### Training Process

The model was trained for 500 epochs. The performance towards the end of the training is as follows:

- **Epoch 500:**
  - Training Accuracy: 78.91%
  - Validation Accuracy: 81.21%

These results indicate fluctuations in training and validation accuracy, suggesting the need for further hyperparameter tuning and potentially more sophisticated data augmentation strategies.

![Loss&Accuracy](images/result1.png)
![Test1](images/result2.png)
![Test2](images/result3.png)

## Real-Time Detection

- By leveraging OpenCV, my system can operate in real-time to determine whether a person is focused on the camera. When attention is detected, a green block appears on the screen.
  **check the real_time_detection.ipynb file for this functionality**

![Test3](images/result4.png)
![Test4](images/result5.png)
