import cv2 
import pytesseract
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('volune', 4)
engine.setProperty('rate', 120)
engine.setProperty('voice', 'french')


img = cv2.imread('test.png')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
print (text);
engine.say(text)
engine.runAndWait()
