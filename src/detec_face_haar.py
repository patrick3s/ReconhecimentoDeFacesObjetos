import cv2

path = 'recursos/'

img = cv2.imread(path+'/fotos/grupo.0.jpg')
classifier = cv2.CascadeClassifier(path+'/recursos/haarcascade_frontalface_default.xml')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces_detect = classifier.detectMultiScale(img_gray,scaleFactor=1.2,minSize=(50,50))
for (x,y,w,h) in faces_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Detectar faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()