import cv2
import face_recognition
import numpy as np

def compare_Faces(img,TrainedFacesList):
    #reduce the image size to 1/4th
    imgS = cv2.resize(img,(0,0), None, 0.25, 0.25)
    
    #change BGR to RGB for face_recognition Library Support
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    #find the Face_Locations from Live Camera
    curFaceLocations = face_recognition.face_locations(imgS)

    #encodings only the certain part of image
    encodingsLiveFace = face_recognition.face_encodings(imgS,curFaceLocations)

    for encode,RtPoints in zip(encodingsLiveFace,curFaceLocations):
        Matches = face_recognition.compare_faces(TrainedFacesList,encode)
        Distance = face_recognition.face_distance(TrainedFacesList,encode)
        # print(Matches)
        # print('D',Distance)
        MatchIndex = np.argmin(Distance)
        MatDis = list(zip(Matches,Distance))
        return (MatchIndex,MatDis,RtPoints)
    return ('No Faces Detected or Not Matching','No Faces Detected or Not matching','No Faces Detected or Not Matching')
 

 
 
    
