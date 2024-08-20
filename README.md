# Navttc-Project-Hand-Land-Marking-Detection

# Hand Detection using MediaPipe and OpenCV

This project demonstrates real-time hand detection and tracking using MediaPipe's Hand solution and OpenCV. The application captures video from your webcam, detects hand landmarks, and tracks them across frames, displaying the results in a window.

## Features

- Detects and tracks up to two hands simultaneously.
- Displays landmarks and connections on detected hands.
- Calculates and displays the FPS (Frames Per Second) of the video stream.
- Flips the video horizontally to provide a mirror-like experience.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Nasir-Sharif/hand-detection-mediapipe-opencv.git
   cd hand-detection-mediapipe-opencv
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required Python packages:

   ```bash
   pip install opencv-python mediapipe times
   ```

## Usage

1. Run the hand detection script:

   ```bash
   python main.py
   ```

2. A window will open, displaying the webcam feed with detected hand landmarks. Press the 'q' key to exit the application.

## Code Overview

```python
import cv2
import time
import mediapipe as mp

cam = cv2.VideoCapture(0)
prev_time = 0

Hand_mp = mp.solutions.hands
Hand_detect = Hand_mp.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    suc, frame = cam.read()
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detect = Hand_detect.process(img_rgb)

    if detect.multi_hand_landmarks:
        for hand in detect.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand, Hand_mp.HAND_CONNECTIONS)
            for id, line_making in enumerate(hand.landmark):
                fh, fw, fc = frame.shape
                x, y = int(fw * line_making.x), int(fh * line_making.y)
                cv2.putText(frame, f'{id}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(frame, f'FPS: {int(fps)}', (30, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1)
    cv2.imshow("WebCam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
```

### Key Points

- **Hand Detection**: Uses MediaPipe to detect up to two hands in real-time and draws the landmarks on the frame.
- **Flipping**: The frame is flipped horizontally for a mirror effect.
- **FPS Calculation**: Calculates and displays the frames per second (FPS) of the video feed.
- **Exiting**: Press 'q' to exit the application.

## Limitations

- The current implementation detects a maximum of two hands. If you need to detect more hands, consider using a different model, such as YOLO, or training a custom model.

## Future Work

- Implement detection for more than two hands using an alternative approach or model.
- Improve performance and accuracy for different lighting conditions.
- Add support for other gestures or hand-related features.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---
