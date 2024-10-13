import firebase_admin
from firebase_admin import credentials,db,storage
import ReadStudentsImages
import cv2
import numpy as np

#Initialize the FireBase Setup to Access - [API]
cred = credentials.Certificate(r"xxx\xxx\xxx\ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxx.firebaseio.com/", #DataBase Name
    'storageBucket':"xxxxxxxxxxxxxxxxxxxxxx.appspot.com"                         #Storage path
})
 

# # StudentImages,StudentIDs = ReadStudentsImages.readStuImg()
# StudentIDs = ReadStudentsImages.readStuImg()[1]

def DetailsToDB():
    ref = db.reference('Students')

    data = {
        '321654' : {
                'Name':'Sundar Pichai',
                'ID':'321654',
                'Starting_Year':'2020',
                'Total_Attendance':6,
                'Standing' : 'G',
                'Year' : '4',
                'Last_Attendance_Time':'0',
                'Major': 'ML'  
                } ,
            '852741' : 
            {
                'Name':'Emily',
                'ID':'321654',
                'Starting_Year':2020,
                'Total_Attendance':6,
                'Standing' : 'G',
                'Year' : 4,
                'Last_Attendance_Time':'0',
                'Major': 'DL'  
                
            },
            '963852' : 
            {
                'Name':'Elon_Musk',
                'ID':'321654',
                'Starting_Year':2020,
                'Total_Attendance':6,
                'Standing' : 'G',
                'Year' : 4,
                'Last_Attendance_Time':'0',
                'Major': 'AI'  
            },
            


    }
    for key,value in data.items():
        ref.child(key).set(value)


def ImagestoStorage():
    #Storing Images
    Images = ReadStudentsImages.getpath()

    #creating Bucket  to Store images in DB
    bucket = storage.bucket()

    for filename in Images:
        blob = bucket.blob(filename)
        blob.upload_from_filename(filename)

def getDetails(id):
    ref = db.reference(f'Students/{id}').get()
    return ref
def getImages(id):
    Images = ReadStudentsImages.getpath()[0].split('/')[0]
    bucket = storage.bucket()
    blob = bucket.get_blob(f'{Images}/{id}.png')
    array = np.frombuffer(blob.download_as_string(),np.uint8)
    imgStudent=cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
    return imgStudent

def Update(id,Atd,last_seen):
    ref = db.reference(f'Students/{id}')
    current_attendance = ref.child('Total_Attendance').get()
    ref.child('Total_Attendance').set(Atd)
    ref.child('Last_Attendance_Time').set(last_seen)

 