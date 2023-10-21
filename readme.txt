# Hand Gesture Recognition Project

## Overview
This project aims to recognize specific hand gestures in real-time using a webcam. It is implemented in Python using the OpenCV and Mediapipe libraries.

## Features
- Real-time hand gesture recognition
- Counts the number of raised fingers (1 to 4)
- Custom thumbs-up gesture to display "Subscribe to Code Depot"

## Requirements
- Python 3.x
- OpenCV 4.5.3
- Mediapipe 0.8.7.3

To install the required packages, you can run:

pip install -r requirements.txt


## Usage
1. Clone the repository
2. Navigate to the project directory
3. Run the command `python main.py` to start the application
4. Press 'q' to quit the application

## How It Works
1. The webcam captures the video feed.
2. Each frame is processed to detect hand landmarks using Mediapipe.
3. The script counts the number of raised fingers and displays it on the screen.
4. A custom thumbs-up gesture displays the message "Subscribe to Code Depot".

## Acknowledgments
- OpenCV (https://opencv.org/)
- Mediapipe by Google (https://google.github.io/mediapipe/)

## License
This project is open-source and available under the MIT License.

## Author
Ankush Saxena