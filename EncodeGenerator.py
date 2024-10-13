import cv2
import face_recognition
import ReadStudentsImages
StudentImages,StudentIDs = ReadStudentsImages.readStuImg()
def KnownFaces():
    TrainedFacesList = []
    for Simg in StudentImages:
        #Convert cv2 image to RGB for face_recognition Module
        img = cv2.cvtColor(Simg,cv2.COLOR_BGR2RGB)

        #Passing the Student Images to face_recognition library for storing the face Identities
        face_encodings = face_recognition.face_encodings(img)[0]

        #Stores the Trained Faces in List
        TrainedFacesList.append(face_encodings)
    return [TrainedFacesList,StudentIDs]
# print(KnownFaces())