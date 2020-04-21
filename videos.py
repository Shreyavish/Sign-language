import cv2

cap=cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()):

    ret,frame = cap.read() #ret will store true /false if frame is available/notavaialable and frame will store and frame will be saved into frame variable
    
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
       
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame',frame) simply read image from webcam
        cv2.imshow('frame',gray) #read in gray mode


        if cv2.waitKey(1) & 0xFF == ord('q'): #when q is pressed close the window
            break
    else:
        break       

cap.release()       