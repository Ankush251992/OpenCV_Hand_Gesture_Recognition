import cv2
import mediapipe as mp

# Initialize Mediapipe's drawing utilities and hands components
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

print("Initializing webcam...")
# Initialize webcam (0 indicates the default webcam)
cap = cv2.VideoCapture(0)

print("Initializing hand detection...")
# Initialize hand detection with a minimum detection confidence of 0.6 and minimum tracking confidence of 0.5
with mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.5) as hands:
    print("Hand detection initialized. Press 'q' to quit.")
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image")
            continue

        # Convert the captured frame from BGR to RGB as Mediapipe uses RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame through Mediapipe Hands
        results = hands.process(rgb_frame)

        # Draw hand landmarks on the frame if any are detected
        if results.multi_hand_landmarks:
            print("Hand(s) detected.")
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Initialize finger count to 0 for each detected hand
                finger_count = 0

                # Define landmarks for finger tips and MCP joints (second joint from the tip)
                tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                        mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
                mcps = [mp_hands.HandLandmark.INDEX_FINGER_MCP, mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                        mp_hands.HandLandmark.RING_FINGER_MCP, mp_hands.HandLandmark.PINKY_MCP]

                # Count the number of raised fingers
                for tip, mcp in zip(tips, mcps):
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[mcp].y:
                        finger_count += 1

                print(f"Finger count: {finger_count}")

                # Check for thumbs-up gesture for the custom message "Subscribe to Code Depot"
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_cmc = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]

                if thumb_tip.y < thumb_cmc.y and thumb_tip.x > thumb_cmc.x:
                    print("Thumbs-up detected. Displaying 'Subscribe to Code Depot'")
                    cv2.putText(frame, "Subscribe to Code Depot", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                                cv2.LINE_AA)
                else:
                    cv2.putText(frame, f"Finger Count: {finger_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2, cv2.LINE_AA)

        # Display the resulting frame with landmarks and labels
        cv2.imshow("Hand Gesture Recognition", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()