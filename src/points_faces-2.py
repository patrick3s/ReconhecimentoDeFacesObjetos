import dlib,cv2
import numpy as np


path = 'recursos/'
def show_lines(img,points_face):
    p68 = [
        [0,16,False],# linha do queixo
        [17,21,False],# sombrancelha direita
        [22,26,False],# sombrancelha esquerda
        [27,30,False],# ponte nasal
        [30,35,True],# nariz inferior
        [36,41,True],# olho esquerdo
        [42,47,True],# olho direito
        [48,59,True],# labio externo
        [60,67,True],# labio interno
    ]   
    for part_face in range(0,len(p68)):
        _points = []
        for index_point_found in range(p68[part_face][0],p68[part_face][1]+1):
            face_point = points_face.part(index_point_found)
            point = [face_point.x,face_point.y]
            _points.append(point)
        _points = np.array(_points,dtype=np.int32)
        cv2.polylines(img,[_points],p68[part_face][2],(255,0,0),2)

fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL
img = cv2.imread(path+'/fotos/grupo.0.jpg')
detector = dlib.get_frontal_face_detector()
detector_points = dlib.shape_predictor(path+'recursos/shape_predictor_68_face_landmarks.dat')
faces_found=detector(img,2)
for face in faces_found:
    points = detector_points(img,face)
    show_lines(img,points)

cv2.imshow("Pontos faciais",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
