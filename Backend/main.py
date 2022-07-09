
import cv2
import pickle
#import cvzone
import numpy as np
 
# Video feed
cap = cv2.VideoCapture(r"D:\projects\Parking Lot Management system with dashboard\video_data\modified_video.mp4")
 
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)
 
# width, height = 107, 48
width, height = 132,71


def image_preprocessing(img):
    """ Takes Raw image & returns dilated image """
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur_img=cv2.GaussianBlur(gray_img,(3,3),1)
    threshold_img=cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian=cv2.medianBlur(threshold_img,5)
    kernel=np.ones((3,3),np.uint8)
    dilate_img=cv2.dilate(imgMedian,kernel,iterations=1)
    return dilate_img




    
 
 
def checkParkingSpace(imgPro):
#     spaceCounter = 0
 
    for pos in posList:
        x, y = pos
 
        imgCrop = imgPro[y:y + height, x:x + width]
        #cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)  

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255,255,255),2)
        cv2.putText(img, str(count), (x, y + height - 3),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1, cv2.LINE_AA)
 
#         if count < 900:
#             color = (0, 255, 0)
#             thickness = 5
#             spaceCounter += 1
#         else:
#             color = (0, 0, 255)
#             thickness = 2
 
        # cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255,255,255),2)
        # cv2.putText(img, str(count), (x, y + height - 3),2,(0,0,0),2)
 
#     cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
#                            thickness=5, offset=20, colorR=(0,200,0))
while True:
 
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):  # IF video ends: then re-run
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    dilate_img=image_preprocessing(img)
    checkParkingSpace(dilate_img)
    cv2.imshow("Image", img)
    # cv2.imshow("imgGray", imgGray)
    #cv2.imshow("Blur", imgBlur)
    #cv2.imshow("ImageThres", imgMedian)
    cv2.waitKey(10)