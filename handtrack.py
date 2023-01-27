import cv2
import mediapipe as mp
import time
cam=cv2.VideoCapture(1)
mpHands= mp.solutions.hands
hands = mpHands.Hands()
mpdarw=mp.solutions.drawing_utils
dict={}
t=[]
pt=ct=0
while True:
    success,img=cam.read()

    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgrgb)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                if id==0:
                    cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)
                if id==4 or id ==8 or id==12 or id==16 or id ==20:
                    cv2.circle(img,(cx,cy),15,(0,0,255),cv2.FILLED)

                if id==0:
                    p=cx
                    q=cy
                if id==8 or id==12 or id==16 or id==20:
                    if p>cx :
                        cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)
                        t.append('green')
                    else:
                        t.append('red')
                    
            print(set(t))
            if set(t)=={'green'}:
                for id,lm in enumerate(handlms.landmark):
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    if id==0:
                        cv2.circle(img,(cx,cy),25,(0,255,0),cv2.FILLED)
                        cv2.putText(img,'RIGHT',(500,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
            if set(t)=={'red'}:
                for id,lm in enumerate(handlms.landmark):
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    if id==0:
                        cv2.circle(img,(cx,cy),25,(0,0,255),cv2.FILLED)
                        cv2.putText(img,'LEFT',(500,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)

            t=[]
   
            mpdarw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)

    ct=time.time()
    fps=1/(ct-pt)
    pt=ct
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
    cv2.imshow("image",img)
    cv2.waitKey(1)