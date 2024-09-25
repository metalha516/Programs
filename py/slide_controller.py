import cv2
import mediapipe as mp
import pyautogui as pg
import time as t
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
                if id == 6:
                 index_x = int((screen_width/frame_width)*x) 
                 index_y = int((screen_height/frame_height)*y) 
                #  pg.moveTo(index_x,index_y)   
                if id == 4:
                 thumb_x = int((screen_width/frame_width)*x) 
                 thumb_y = int((screen_height/frame_height)*y)
            if (70 < abs(index_x-thumb_x) < 150):
                   pg.press('left')
                   t.sleep(1)
    cv2.imshow("camera", frame)
    cv2.waitKey(1)