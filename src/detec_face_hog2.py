import cv2,dlib

path = 'recursos/'

sub_detector = ["Olhar a frente","Vista a esquerda","Vista a direita",
                "A rente girando a esquerda","A frente girando a direita"]
img = cv2.imread(path+'/fotos/grupo.0.jpg')
detector = dlib.get_frontal_face_detector()
facesFounds, scores, idx = detector.run(img)

for index,face in enumerate(facesFounds):
    l,t,r,b = [int(face.left()),int(face.top()),int(face.right()),int(face.bottom())]
    cv2.rectangle(img,(l,t),(r,b), (0,255,255),2)
    print(f"Pontuação: {scores[1]} Sub-Detector: {sub_detector[idx[index]]} Face: {face}")

cv2.imshow("Face hog",img)
cv2.waitKey(0)
cv2.destroyAllWindows()