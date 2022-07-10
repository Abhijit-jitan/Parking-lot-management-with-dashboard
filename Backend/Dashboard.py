import cv2,datetime


def realtime_dashboard(blank_dashboard):

    dash=cv2.imread(r"D:\projects\Parking Lot Management system with dashboard\Backend\inferenced_frames\saved_dash.png")
    single_line="_"*100
    double_line="="*100

    ## current date & time 
    now=datetime.datetime.now()
    date=now.strftime("%b %d, %Y")
    time=now.strftime("%H:%M:%S")
    heading_font,subheading_font,normal=cv2.FONT_HERSHEY_COMPLEX_SMALL,cv2.FONT_HERSHEY_COMPLEX_SMALL,cv2.FONT_HERSHEY_SIMPLEX

    ## main heading
    cv2.putText(dash, "PARKING MANAGEMENT",(23,45),heading_font,fontScale=1.6,thickness=3,color=(0,0,0))
    cv2.putText(dash, "Dashboard",(140,80),heading_font,fontScale=1.55,thickness=3,color=(0,0,0))
    cv2.putText(dash, double_line,(0,110),normal,fontScale=.5,thickness=1,color=(0,0,0))

    ## date & time
    cv2.putText(dash, "Date:",(5,160),normal,fontScale=1,thickness=3,color=(0,0,0))
    cv2.putText(dash, str(date),(95,160),normal,fontScale=1,thickness=2,color=(0,0,0))
    cv2.putText(dash, str(time),(330,160),normal,fontScale=1,thickness=2,color=(0,0,0))

    ## Live status of General parking sopt
    cv2.putText(dash, "Free Parking Space: ",(5,220),normal,fontScale=1,thickness=3,color=(0,0,255))
    cv2.putText(dash, single_line,(0,233),normal,fontScale=2,thickness=2,color=(0,0,0))
    cv2.putText(dash, "Block A : ",(15,275),normal,fontScale=1,thickness=3,color=(0,0,0))
    cv2.putText(dash, "Block B : ",(15,310),normal,fontScale=1,thickness=3,color=(0,0,0))
    cv2.putText(dash, "Block C : ",(15,350),normal,fontScale=1,thickness=3,color=(0,0,0))
    cv2.putText(dash, "Block D : ",(15,390),normal,fontScale=1,thickness=3,color=(0,0,0))

    ## Live status of Special parking sopt
    cv2.putText(dash, "Free Special Parking Space: ",(5,450),normal,fontScale=1,thickness=3,color=(0,0,255))
    cv2.putText(dash, single_line,(0,463),normal,fontScale=2,thickness=2,color=(0,0,0))
    cv2.putText(dash, "Block A-Special : ",(15,500),normal,fontScale=1,thickness=3,color=(0,0,0))
    cv2.putText(dash, "Block B-Special : ",(15,540),normal,fontScale=1,thickness=3,color=(0,0,0))
    cv2.putText(dash, "Block C-Special : ",(15,580),normal,fontScale=1,thickness=3,color=(0,0,0))
    cv2.putText(dash, "Block D-Special : ",(15,620),normal,fontScale=1,thickness=3,color=(0,0,0))

    ## Live Bargraph
    cv2.putText(dash, "Real time Graph: ",(5,680),normal,fontScale=1,thickness=3,color=(0,0,255))
    cv2.putText(dash, single_line,(0,694),normal,fontScale=2,thickness=2,color=(0,0,0))


    #cv2.imwrite(r"D:\projects\Parking Lot Management system with dashboard\Backend\inferenced_frames\saved_dash_.png",dash)
    return dash


#cv2.waitKey(0)
