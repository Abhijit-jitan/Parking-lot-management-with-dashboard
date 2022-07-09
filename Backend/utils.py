
import cv2
def parking_lot_daetails(img):
    #img = cv2.imread(img)
    cv2.putText(img,"Block-A",(245,1017),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),8,cv2.LINE_AA)
    cv2.rectangle(img,(162,1),(427,253),(255,0,255),5)       # Special Block-A
    


    cv2.imshow("Image", img)
    cv2.waitKey(0)


img = cv2.imread(r"D:\projects\Parking Lot Management system with dashboard\video_data\frames\1.jpg")
parking_lot_daetails(img)
    

