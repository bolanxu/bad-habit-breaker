import cv2
import mediapipe as mp
import math
import time
from pygame import mixer

# 1. Initialize Pygame mixer
mixer.init()
try:
    mixer.music.load('warning.mp3')
except:
    print("Warning: 'warning.mp3' not found.")

# 2. Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

TRIGGER_DISTANCE = 0.09 
sound_cooldown = 1.5 
last_played = 0

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_count = 0
process_every_n_frames = 2 

# Global state tracker
triggered = False

with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=False) as face_mesh, \
     mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frame_count += 1
        frame = cv2.flip(frame, 1)
        
        # Only do heavy AI math every N frames
        if frame_count % process_every_n_frames == 0:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_results = face_mesh.process(rgb_frame)
            hand_results = hands.process(rgb_frame)

            mouth_lip = None
            hand_points = []

            # 1. Reset the trigger state every time we actually check the camera
            triggered = False 

            if face_results.multi_face_landmarks:
                mouth_lip = face_results.multi_face_landmarks[0].landmark[13]

            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    hand_points.append(hand_landmarks.landmark[4])  # Thumb
                    hand_points.append(hand_landmarks.landmark[8])  # Index
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 2. Check distances only if both are present
            if mouth_lip and hand_points:
                for point in hand_points:
                    distance = math.sqrt((point.x - mouth_lip.x)**2 + (point.y - mouth_lip.y)**2)
                    if distance < TRIGGER_DISTANCE:
                        triggered = True
                        break

        # UI
        if triggered:
            cv2.putText(frame, "STOP!", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if time.time() - last_played > sound_cooldown:
                try:
                    mixer.music.play()
                    last_played = time.time()
                except:
                    pass
        else:
            cv2.putText(frame, "Safe", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        small_frame = cv2.resize(frame, (320, 240))
        cv2.imshow('Habit Breaker Cam', small_frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()