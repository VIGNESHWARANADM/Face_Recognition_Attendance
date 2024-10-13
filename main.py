#python modules               #Custom Modules
import cv2                    # import cvzone
import pickle                 # import face_recognition
#Custom Modules               # import os
import ReadModeImages         # import matplotlib
import PickleDump             # import numpy as np
import Compare_Faces          # import ReadStudentsImages
import rectangle              
import FireBase
import SwitchModes
import DateTime


#Store Student Images to Firestore DataBase
FireBase.ImagestoStorage()

#Store Student Details to RealTime DataBase
FireBase.DetailsToDB()

#store Different Modes of Images in List
ModeImages = ReadModeImages.readModes()

#store Student Images and IDs in List
# StudentImages,StudentIDs = ReadStudentsImages.readStuImg()

#Create and Load the Pickle File
picklecreate = PickleDump.PickleCreation()
file = open(picklecreate,'rb')
KnownFacesList = pickle.load(file)
TrainedFacesList,StudentIDs = KnownFacesList

# cap
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)   # Set height

imgBackground = cv2.imread(r"D:\XXXXXXXXX\background.png")

while True:
    success, img = cap.read()
    
    #image overlay - Camera
    imgBackground[162:162+ 480, 55:55+ 640] = img
    #image overlay - Modes
    imgBackground[44:44+ 633, 808:808+ 414] = ModeImages[1]


    if not success:
        break  # Break the loop if there's an issue with capturing

    #Compare the Faces
    argmin,MatDis,RectangleP = Compare_Faces.compare_Faces(img,TrainedFacesList)

    #Get the ID of Matched Faces
    MatchedID = StudentIDs[argmin] if (type(argmin) != str and MatDis[argmin][0] and type(MatDis)!= str)  else False

    #Rectangle Box Fitting
    if MatchedID:
        
        #Import Student Details from FireBase
        getStudentDetails = FireBase.getDetails(MatchedID)
        #Time Management
        curTime = DateTime.TimeDateCur()
        LastSeen = getStudentDetails['Last_Attendance_Time']
        if LastSeen == '0':
            i=2
            imgBackground[44:44+ 633, 808:808+ 414] = ModeImages[i]
        elif LastSeen != '0': 
             i = 3
            #  imgBackground[44:44+ 633, 808:808+ 414] = ModeImages[i]
             #Student Photo - Overlay
             imgBackground[175:175+216,909:909+216] = FireBase.getImages(MatchedID)
            #  print(DateTime.TD(curTime,LastSeen))
        #Update Data to FireBase
        FireBase.Update(MatchedID,getStudentDetails['Total_Attendance'],DateTime.TimeDateCur())

        #Put Rectangle Border
        imgBackground = rectangle.CreateRectangle(RectangleP,imgBackground)
        # imgBackground[175:175+216,909:909+216] = FireBase.getImages(MatchedID)

        SwitchModes.Tot_At(imgBackground,getStudentDetails) #display total attendance
        SwitchModes.Major(imgBackground,getStudentDetails)  #display majore
        SwitchModes.ID(imgBackground,getStudentDetails)     #display ID
        SwitchModes.Standing(imgBackground,getStudentDetails) #display Standing
        SwitchModes.Name(imgBackground,getStudentDetails)     #display Name
        SwitchModes.Starting_Year(imgBackground,getStudentDetails)  #display Batch

        
    cv2.imshow('Face Attendance',imgBackground)
    # cv2.imshow('Webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()

