import cv2
import mediapipe as mp
import pyautogui as pg
cam = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw = mp.solutions.drawing_utils
screen_width, screen_height = pg.size()
while True:
    _,frame= cam.read()
    frame_height, frame_width, _ = frame.shape
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result=hands.process(frame_rgb)
    landmarks = (result.multi_hand_landmarks)
    if landmarks:
        for landmark in landmarks:
            draw.draw_landmarks(frame, landmark, mp_hands.HAND_CONNECTIONS)
            hand_landmarks = landmark.landmark
            for id, hand_landmark in enumerate(hand_landmarks):
                x = int(hand_landmark.x*frame_width)
                y = int(hand_landmark.y*frame_height)
                if id == 8:
                 index_x = (screen_width/frame_width)*x 
                 index_y = (screen_height/frame_height)*y 
                 pg.moveTo(index_x,index_y)   
                if id == 12:
                 middle_x = (screen_width/frame_width)*x 
                 middle_y = (screen_height/frame_height)*y 
                 if (abs(middle_x - index_x) < 60):
                    pg.click()
    cv2.imshow("camera", frame)
    cv2.waitKey(1)