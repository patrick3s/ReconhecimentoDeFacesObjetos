path = 'recursos/'

# para executar esse  script é recomendado usar uma maquina com bom processamento de gpu
import cv2
import dlib
#quanto maior a escala maior a quantidade de faces detectadas porém aumenta o processamento de mais
scale_img =0
img = cv2.imread(path+'/fotos/grupo.0.jpg')
detector = dlib.cnn_face_detection_model_v1(path+'recursos/mmod_human_face_detector.dat')
faces_found = detector(img,scale_img)
for face in faces_found:
    l,t,r,b,c =[int(face.rect.left()),int(face.rect.top()),int(face.rect.right()),int(face.rect.bottom()),face.confidence]
    cv2.rectangle(img,(l,t),(r,b),(255,255,0),2)
cv2.imshow("Detector CNN",img)
cv2.waitKey(0)
cv2.destroyAllWindows()