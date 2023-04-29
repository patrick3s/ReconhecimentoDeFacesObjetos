import dlib,cv2

path = 'recursos/'
def show_points(img,points):
    for p in points.parts():
        cv2.circle(img,(p.x,p.y),2,(0,255,0),2)

fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL
img = cv2.imread(path+'/fotos/grupo.0.jpg')
detector = dlib.get_frontal_face_detector()
detector_points = dlib.shape_predictor(path+'recursos/shape_predictor_68_face_landmarks.dat')
faces_found=detector(img,2)
for face in faces_found:
    points = detector_points(img,face)
    show_points(img,points)

cv2.imshow("Pontos faciais",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
