import mediapipe as mp
import cv2

cam = cv2.VideoCapture(0)
hands = mp.solutions.hands
hands_detector = hands.Hands()
mp_Draw = mp.solutions.drawing_utils
while True:
    _,frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands_detector.process(frame)
    landmarks = result.multi_hand_landmarks
    if landmarks : 
        for landmark in landmarks:
            mp_Draw.draw_landmarks(frame, landmark, hands.HAND_CONNECTIONS)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)