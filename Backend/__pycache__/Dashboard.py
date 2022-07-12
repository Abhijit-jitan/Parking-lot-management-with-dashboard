import cv2,datetime
import numpy as np

# blank_dashboard=np.zeros([1080,480,3],dtype=np.uint8)            # (1080, 480, 3)  # (frame_height,width)
# blank_dashboard.fill(255)

def realtime_dashboard(dash,count_A,count_B,count_C,count_D,count_As):
    heading_font_scale,subhead_font_scale,font_scale=1.25,0.85,0.75
    heading_thickness,thickness1,thickness2=4,3,2
    heading_font,font=cv2.FONT_HERSHEY_DUPLEX,cv2.FONT_HERSHEY_SIMPLEX
    
    double_line,single_line="="*100,"_"*100

    ## current date & time 
    now=datetime.datetime.now()
    date=now.strftime("%b %d, %Y")
    time=now.strftime("%H:%M:%S")
    ## main heading
    cv2.putText(dash, "PARKING MANAGEMENT",(12,45),heading_font,heading_font_scale,(0,0,0),heading_thickness)
    cv2.putText(dash, "Dashboard",(142,85),heading_font,heading_font_scale,(0,0,0),heading_thickness)
    cv2.putText(dash, double_line,(0,130),font,font_scale,(0,0,0),thickness2)

    ## date & time
    cv2.putText(dash, "Date: {}".format(str(date)),(55,180),font,subhead_font_scale,(0,0,0),thickness1)
    cv2.putText(dash, "Time: {}".format(str(time)),(55,220),font,subhead_font_scale,(0,0,0),thickness1)
    cv2.putText(dash, single_line,(0,250),font,fontScale=font_scale,thickness=thickness2,color=(0,0,0))
    
    # ## Live status of General parking sopt
    cv2.putText(dash, "Available Parking Space",(46,305),font,1,(0,0,255),3)
    cv2.putText(dash, "Block A: {}/18".format(count_A),(2,350),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, "Block A-unique: {}/4".format(count_As),(207,350),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, "Block B: {}/24".format(count_B),(2,385),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, "Block B-unique: None",(207,385),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, "Block C: {}/22".format(count_C),(2,420),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, "Block C-unique: None",(207,420),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, "Block D: {}/23".format(count_D),(2,455),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, "Block D-unique: None",(207,460),font,font_scale,(0,0,0),thickness2)
    cv2.putText(dash, single_line,(0,490),font,fontScale=font_scale,thickness=thickness2,color=(0,0,0))

    ## Live Bargraph
    cv2.putText(dash, "Real time Graph ",(100,540),font,1,(0,0,255),3)
    
    return dash,time

# blank_dashboard=cv2.imread("/home/ryan/Projects/Parking Lot Management system with dashboard/Backend/blank_.png")
# real_time_dash=realtime_dashboard(dash,count_A,count_B,count_C,count_D,count_As)
# real_time_dash=realtime_dashboard(blank_dashboard,4,2,1,2,3)
# cv2.imwrite(r"D:\projects\Parking Lot Management system with dashboard\Backend\inferenced_frames\test.png",real_time_dash)