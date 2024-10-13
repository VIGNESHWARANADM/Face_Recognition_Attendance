import cv2
import os
def readStuImg():
    cwd = os.getcwd()
    pathjoin = os.path.join(cwd,'StudentImages')
    listdir = os.listdir(pathjoin)
    readImages = []
    StudentIDs = []
    # readImagesdict = {}
    for i in listdir:
        img = cv2.imread(rf'{pathjoin}\{i}')
        readImages.append(img)
        StudentIDs.append(i.split('.')[0])
        # readImagesdict[os.path.splitext(i)[0]] = img
        
    return (readImages,StudentIDs)

# print(readStuImg())
def getpath():
    cwd = os.getcwd()
    pathjoin = os.path.join(cwd,'StudentImages')
    listdir = os.listdir(pathjoin)
    Paths = []
    for i in listdir:
        Paths.append(f'{pathjoin}/{i}')
    return Paths
print(getpath())