import cv2
import numpy as np
import mediapipe as mp

# Initialize Mediapipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Drawing parameters
drawing_color = (0, 0, 255)  # Red color
drawing_thickness = 5

# Variables for drawing
drawing = False
last_position = None

# Set up webcam
cap = cv2.VideoCapture(0)

# Initialize Mediapipe Hands
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    # Canvas to draw on
    canvas = np.zeros((480, 640, 3), dtype=np.uint8)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for easier drawing experience
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get the coordinates of the index finger tip (Landmark 8)
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, c = frame.shape
                index_tip_position = (int(index_tip.x * w), int(index_tip.y * h))

                # Start drawing when the index finger tip is detected
                if drawing:
                    if last_position is not None:
                        # Draw a line from the last position to the current position
                        cv2.line(canvas, last_position, index_tip_position, drawing_color, drawing_thickness)
                    last_position = index_tip_position
                else:
                    last_position = None

                # Check if thumb and index are close to simulate "pen down"
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_tip_position = (int(thumb_tip.x * w), int(thumb_tip.y * h))
                distance = np.linalg.norm(np.array(index_tip_position) - np.array(thumb_tip_position))

                # If distance is small, activate drawing mode
                if distance < 30:
                    drawing = True
                else:
                    drawing = False

                # Draw hand landmarks for reference (optional)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Overlay the canvas on the frame
        combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

        # Display the output
        cv2.imshow("Finger Stylus Notes", combined)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()