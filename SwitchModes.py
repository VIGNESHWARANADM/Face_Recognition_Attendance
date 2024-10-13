import ReadModeImages
import cv2



ModeImages = ReadModeImages.readModes()

def Tot_At(imgBackground,getStudentDetails):
    Text = cv2.putText(imgBackground,str(getStudentDetails['Total_Attendance']),(861,125),
                       cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    return Text

def Name(imgBackground,getStudentDetails):
    (w,h),_ = cv2.getTextSize(getStudentDetails['Name'],cv2.FONT_HERSHEY_COMPLEX,1,1)
    offset = (414-w)//2
    Text = cv2.putText(imgBackground,getStudentDetails['Name'],(808+offset,445),
                       cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50),1)
    return Text

def Major(imgBackground,getStudentDetails):
    Text = cv2.putText(imgBackground,getStudentDetails['Major'],(1006,550),
                       cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    return Text

def ID(imgBackground,getStudentDetails):
    Text = cv2.putText(imgBackground,getStudentDetails['ID'],(1006,493),
                       cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    return Text

def Standing(imgBackground,getStudentDetails):
    Text = cv2.putText(imgBackground,getStudentDetails['Standing'],(910,625),
                       cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
    return Text
def Starting_Year(imgBackground,getStudentDetails):
    Text = cv2.putText(imgBackground,str(getStudentDetails['Starting_Year']),(1125,625),
                       cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
    return Text
def Year(imgBackground,getStudentDetails):
    Text = cv2.putText(imgBackground,getStudentDetails['Year'],(1025,625),
                       cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
    return Text
 