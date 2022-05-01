import cv2
import pytesseract
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 100)
engine.setProperty('volune', 4)
engine.setProperty('rate', 100)
engine.setProperty ('voice','french')

#pytesseract.pytesseract.tesseract_cmd = '/usr/local/share/tessdata/fra.traineddata'

video =cv2.VideoCapture(1)
video.set(3, 640)
video.set(4, 480)

img1 = cv2.imread('images/img1.png')
height_img, width_img, _ = img1.shape

box1 = pytesseract.image_to_boxes(img1)

data1 = pytesseract.image_to_data(img1)

while True :
    check, frame = video.read()
    data = pytesseract.image_to_data(frame)
    dat = pytesseract.image_to_string(frame)
    for z,a in enumerate (data.splitlines()) :
        if z != 0:
            a = a.split()

            if len(a) == 12:
                x, y = int(a[6]),int(a[7])
                z, t = int(a[8]),int(a[9])
                cv2.rectangle(frame,(x, y),(x + z, y + t),(255,0,0),1)

    cv2.imshow('Capture video ', frame)
    
    engine.say(dat)
    engine.runAndWait()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
#for z,a in enumerate (data1.splitlines()) :
#    if z != 0:
#        a = a.split()

#        if len(a) == 12:
#            x, y = int(a[6]),int(a[7])
#            z, t = int(a[8]),int(a[9])
#            cv2.rectangle(img1,(x, y),(x + z, y + t),(255,0,0),1)

#cv2.imshow('image test', img1)
#cv2.waitKey(0)
print (pytesseract.image_to_string(img1))
