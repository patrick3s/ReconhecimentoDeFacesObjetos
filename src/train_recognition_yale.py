import cv2,glob,dlib,os
import pickle as pk
import numpy as np
from PIL import Image
path = 'recursos/'

detector_face = dlib.get_frontal_face_detector()
detector_points = dlib.shape_predictor(path+"recursos/shape_predictor_68_face_landmarks.dat")
recognition_face = dlib.face_recognition_model_v1(path+"recursos/dlib_face_recognition_resnet_model_v1.dat")

indices = {}
idx = 0
describe_faces = None

for file in glob.glob(os.path.join(path+"yalefaces/treinamento","*.jpg")):
    img = Image.open(file).convert("RGB")
    img = np.array(img,'uint8')
    faces_found = detector_face(img,1)
    num_faces_detecteds = len(faces_found)
    if num_faces_detecteds > 1:
        print(f'Há mais de uma face na image {file}')
        exit(0)
    elif num_faces_detecteds < 1:
        print('Nenhuma face encontrada no arquivo {file}')
        exit(0)
    
    for face in faces_found:
        points_face = detector_points(img,face)
        describe_face = recognition_face.compute_face_descriptor(img,points_face)
        list_describe_face = [df for df in describe_face]
        np_array_describe_face = np.asarray(list_describe_face,dtype=np.float64)
        np_array_describe_face = np_array_describe_face[np.newaxis, :]
        if describe_faces is None:
            describe_faces = np_array_describe_face
        else:
            describe_faces = np.concatenate((describe_faces,np_array_describe_face),axis=0)
        indices[idx] = file
        idx+=1

np.save(path+"recursos/descritores_rn_yale.npy",describe_faces)
with open(path+"recursos/indices_rn_yale.pickle",'wb') as f:
    pk.dump(indices,f)



