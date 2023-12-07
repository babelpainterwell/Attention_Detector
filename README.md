# Enhancing AI-Human Interaction: Introducing the Eye Contact Recognition ModelEnhancing AI-Human Interaction: Introducing the Eye Contact Recognition Model

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

## Results

![Loss&Accuracy](images/result1.png)
![Test1](images/result2.png)
![Test2](images/result3.png)

## Notes

- By leveraging OpenCV, our system can operate in real-time to determine whether a person is focused on the camera. When attention is detected, a green block appears on the screen.
  **check the real_time_detection.ipynb file for this functionality**

![Test3](images/result4.png)
![Test4](images/result5.png)
