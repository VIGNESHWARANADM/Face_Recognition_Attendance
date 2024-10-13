import cv2
import os

def readModes():
    cwd = os.getcwd()
    pathjoin = os.path.join(cwd,'ModeImages')
    path = os.listdir(pathjoin)
    imread = []  
    for i in path:
        img = cv2.imread(rf'{pathjoin}\{i}')
        imread.append(img)
    return imread
     
