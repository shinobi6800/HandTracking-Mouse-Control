import cv2
import mediapipe as mp
import pyautogui

# Set up MediaPipe hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cam = cv2.VideoCapture(0)

# Get screen resolution
screen_width, screen_height = pyautogui.size()

while True:
    success, frame = cam.read()
    if not success:
        break

    # Flip the image horizontally for natural interaction
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        # Index finger tip (landmark 8)
        x = int(hand_landmarks.landmark[8].x * w)
        y = int(hand_landmarks.landmark[8].y * h)

        # Convert to screen coordinates
        screen_x = int(hand_landmarks.landmark[8].x * screen_width)
        screen_y = int(hand_landmarks.landmark[8].y * screen_height)

        # Move the mouse
        pyautogui.moveTo(screen_x, screen_y)

        # Draw hand landmarks
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.circle(frame, (x, y), 10, (255, 0, 255), cv2.FILLED)

    # Show webcam feed
    cv2.imshow("Hand Mouse Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
