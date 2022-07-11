import cv2
import pickle
 
width, height = 132,86

try:
    with open(r'Parking-lot locations/parking_position_block-A_special', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
 
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
 
    with open(r'Parking-lot locations/parking_position_block-A_special', 'wb') as f:
        pickle.dump(posList, f)
 
 
while True:
    img = cv2.imread(r"D:\projects\Parking Lot Management system with dashboard\Backend\parking_lot_structure.jpg")
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
 
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)


