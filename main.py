import cv2
import time
import mediapipe as mp


cam =cv2.VideoCapture(0)
prev_time =0

Hand_mp = mp.solutions.hands
Hand_detect = Hand_mp.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    suc, frame= cam.read()
    frame = cv2.flip(frame, 1)
    img_rgb =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detect = Hand_detect.process(img_rgb)


    if detect.multi_hand_landmarks :
        for hand in detect.multi_hand_landmarks :
            mpDraw.draw_landmarks(frame, hand, Hand_mp.HAND_CONNECTIONS)
            for id, line_making in enumerate(hand.landmark):
                fh, fw,fc = frame.shape 
                x,y = int(fw*line_making.x), int (fh*line_making.y)
                cv2.putText(frame, f'{id}', (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)  #this will hightlight the points in the hand it will make the bubles and colors them using the function from mediapipe and using the cv functions

    curr_time = time.time()
    fps = 1/(curr_time-prev_time)   #this will capture the frames wheather they are 20,23,30 etc
    prev_time = curr_time
    
    cv2.putText(frame, f'Total_FPS: {int(fps)}',(30,30), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 1 )

    cv2.imshow("Real_time_webCam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindow()


