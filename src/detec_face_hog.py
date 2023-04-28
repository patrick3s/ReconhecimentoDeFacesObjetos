import cv2,dlib

path = 'recursos/'

img = cv2.imread(path+'/fotos/grupo.0.jpg')
detector = dlib.get_frontal_face_detector()
facesFounds = detector(img)
for face in facesFounds:
    l,t,r,b = [int(face.left()),int(face.top()),int(face.right()),int(face.bottom())]
    cv2.rectangle(img,(l,t),(r,b), (0,255,255),2)
cv2.imshow("Detectar faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
