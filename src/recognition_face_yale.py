import cv2,glob,dlib,os
import pickle as pk
import numpy as np
path = 'recursos/'

detector_face = dlib.get_frontal_face_detector()
detector_points = dlib.shape_predictor(path+"recursos/shape_predictor_68_face_landmarks.dat")
recognition_face = dlib.face_recognition_model_v1(path+"recursos/dlib_face_recognition_resnet_model_v1.dat")

indices = np.load(path+"recursos/indices_rn.pickle",allow_pickle=True)
limiar = 0.5
describe_faces = np.load(path+"recursos/descritores_rn.npy")

for file in glob.glob(os.path.join(path+"fotos","*.jpg")):
    img = cv2.imread(file)
    faces_found = detector_face(img,2)
    for face in faces_found:
        l,t,r,b = (int(face.left()),int(face.top()),int(face.right()),int(face.bottom()))
        points_face = detector_points(img,face)
        describe_face = recognition_face.compute_face_descriptor(img,points_face)
        list_describe_face = [fd for fd in describe_face]
        np_array_descriptor_face = np.asarray(list_describe_face,dtype=np.float64)
        np_array_descriptor_face = np_array_descriptor_face[np.newaxis, :]
        distance = np.linalg.norm(np_array_descriptor_face - describe_faces,axis=1)
        _min = np.argmin(distance)
        distance_min = distance[_min]
        if distance_min <= limiar:
            nome = os.path.split(indices[_min])[1].split(".")[0]
        else:
            nome = ' '
        
        cv2.rectangle(img,(l,t),(r,b),(0,255,255),2)
        text = f"{nome} {distance_min:.4f}"
        cv2.putText(img,text,(r,t),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,255,255))
    cv2.imshow("Reconhecimento de ffaces hog",img)
    cv2.waitKey(0)

cv2.destroyAllWindows()





