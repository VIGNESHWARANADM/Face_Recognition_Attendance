import cvzone

def CreateRectangle(points,img):
    y1, x2, y2, x1 = points
    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
    bbox = (55 + x1, 162 + y1, (x2 - x1), (y2 - y1))
    imgBackground = cvzone.cornerRect(img,bbox,rt = 0)
    return imgBackground