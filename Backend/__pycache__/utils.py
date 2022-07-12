import cv2,pickle
import numpy as np

width, height = 132,71
widthS, heightS = 135,79


def parking_lot_daetails(img):
    #img = cv2.imread(img)
    cv2.putText(img,"Block-A",(246,1066),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3,cv2.LINE_AA)
    cv2.rectangle(img,(162,1),(427,253),(255,0,255),5)       # Special Block-A
    resized_img=cv2.resize(img,(1680,900))
    cv2.imshow("Image", resized_img)
    cv2.waitKey(0)
# img = cv2.imread(r"/home/ryan/Projects/Parking Lot Management system with dashboard/video_data/frames/0.jpg")
# parking_lot_daetails(img)


def image_preprocessing(img):
    """ Takes Raw image & returns dilated image """
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur_img=cv2.GaussianBlur(gray_img,(3,3),1)
    threshold_img=cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian=cv2.medianBlur(threshold_img,5)
    kernel=np.ones((3,3),np.uint8)
    dilate_img=cv2.dilate(imgMedian,kernel,iterations=1)
    return dilate_img
#image_preprocessing(img)


  
def verify_parkinglot_block_A(imgPro,img):
    with open(r'D:\projects\Parking Lot Management system with dashboard\Backend\Parking-lot locations\parking_position_block-A','rb') as f:
        block_A= pickle.load(f) 

    spaceCounterA = 0
 
    for posA in block_A:
        x, y = posA
        imgCrop = imgPro[y:y + height, x:x + width]
        #cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)  
        
        if count<1000:
            color,thickness=(0,255,0),2
            spaceCounterA += 1
        else:
            color,thickness=(0,0,255),2
 
        cv2.rectangle(img,posA,(posA[0]+width,posA[1]+height),color,thickness)
        cv2.putText(img, str(count), (x, y + height - 3),cv2.FONT_HERSHEY_SIMPLEX,1,color,1, cv2.LINE_AA)
    return spaceCounterA



def verify_parkinglot_block_special_A(imgPro,img):
    with open(r'D:\projects\Parking Lot Management system with dashboard\Backend\Parking-lot locations\parking_position_block-A_special', 'rb') as f:
        block_A_special= pickle.load(f) 

    spaceCounterAs = 0
 
    for posA in block_A_special:
        x, y = posA
        imgCrop = imgPro[y:y + heightS, x:x + widthS]
        #cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)  
        
        if count<1000:
            color,thickness=(0,255,0),2
            spaceCounterAs += 1
        else:
            color,thickness=(0,0,255),2
 
        cv2.rectangle(img,posA,(posA[0]+widthS,posA[1]+heightS),color,thickness)
        cv2.putText(img,str(count),(x,y+heightS-2),cv2.FONT_HERSHEY_SIMPLEX,1,color,1,cv2.LINE_AA)
    return spaceCounterAs



def verify_parkinglot_block_B(imgPro,img):
    with open(r'D:\projects\Parking Lot Management system with dashboard\Backend\Parking-lot locations\parking_position_block-B', 'rb') as f:
        block_B= pickle.load(f) 

    spaceCounterB = 0
 
    for posB in block_B:
        x, y = posB
        imgCrop = imgPro[y:y + height, x:x + width]
        #cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)  
        
        if count<1000:
            color,thickness=(0,255,0),2
            spaceCounterB += 1
        else:
            color,thickness=(0,0,255),2
 
        cv2.rectangle(img,posB,(posB[0]+width,posB[1]+height),color,thickness)
        cv2.putText(img, str(count), (x, y + height - 2),cv2.FONT_HERSHEY_SIMPLEX,1,color,1, cv2.LINE_AA)
    return spaceCounterB



def verify_parkinglot_block_C(imgPro,img):
    with open(r'D:\projects\Parking Lot Management system with dashboard\Backend\Parking-lot locations\parking_position_block-C', 'rb') as f:
        block_C= pickle.load(f) 

    spaceCounterC = 0
 
    for posC in block_C:
        x, y = posC
        imgCrop = imgPro[y:y + height, x:x + width]
        #cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)  
        
        if count<1400:
            color,thickness=(0,255,0),2
            spaceCounterC += 1
        else:
            color,thickness=(0,0,255),2
 
        cv2.rectangle(img,posC,(posC[0]+width,posC[1]+height),color,thickness)
        cv2.putText(img, str(count), (x, y + height - 3),cv2.FONT_HERSHEY_SIMPLEX,1,color,1, cv2.LINE_AA)
        #cv2.putText(img,str(count),(x,y+height-3),2,(0,0,0),2)
    return spaceCounterC 



def verify_parkinglot_block_D(imgPro,img):
    with open(r'D:\projects\Parking Lot Management system with dashboard\Backend\Parking-lot locations\parking_position_block-D', 'rb') as f:
        block_D= pickle.load(f) 

    spaceCounterD = 0

    for posD in block_D:
        x, y = posD
        imgCrop = imgPro[y:y + height, x:x + width]
        #cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)  
        
        if count<1300:
            color,thickness=(0,255,0),2
            spaceCounterD += 1
        else:
            color,thickness=(0,0,255),2
 
        cv2.rectangle(img,posD,(posD[0]+width,posD[1]+height),color,thickness)
        cv2.putText(img, str(count), (x, y + height - 3),cv2.FONT_HERSHEY_SIMPLEX,1,color,1, cv2.LINE_AA)
    return spaceCounterD


    

