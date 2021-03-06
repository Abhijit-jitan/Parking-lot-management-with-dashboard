
import cv2,pickle,os,datetime
import numpy as np
from utils import image_preprocessing,verify_parkinglot_block_A,verify_parkinglot_block_special_A,verify_parkinglot_block_B,verify_parkinglot_block_C,verify_parkinglot_block_D
from Dashboard import realtime_dashboard
from realtime_graph import realtime_csv_generate,make_realtime_graph
import pandas as pd

now=datetime.datetime.now()
date=now.strftime("%b %d, %Y")    


## Main_function
cap=cv2.VideoCapture(r"D:\projects\Parking Lot Management system with dashboard\video_data\modified_video.mp4")
frame_no=0
while True:
 
    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):     # If video ends: then re-run
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success,img=cap.read()

    dilate_img=image_preprocessing(img)                              # preprocess image
    
    ## Count free-parking space in All Blocks
    count_A=verify_parkinglot_block_A(dilate_img,img)
    count_As=verify_parkinglot_block_special_A(dilate_img,img) 
    count_B=verify_parkinglot_block_B(dilate_img,img)
    count_C=verify_parkinglot_block_C(dilate_img,img)
    count_D=verify_parkinglot_block_D(dilate_img,img)
    
    ## create Blank-Dashboard
    blank_dashboard=np.zeros([1080,480,3],dtype=np.uint8)            # (1080, 480, 3)  # (frame_height,width)
    blank_dashboard.fill(255)

    ## Write & load Realtime Dashboard
    dashboard,time=realtime_dashboard(blank_dashboard,count_A,count_B,count_C,count_D,count_As)
    with_dashboard=np.concatenate((img,dashboard),axis=1)            # Vstack of inference & realtime dashboard
    
    ## Realtime data append to csv
    df={"Date":date,"time":time,"A":[count_A],"As":[count_As],"B":[count_B],"C":[count_C],"D":[count_D]}
    realtime_csv_generate(df)

    ## Realtime bar-graph
    df_realtime=pd.read_csv(r"D:\projects\Parking Lot Management system with dashboard\Backend\csv\data.csv")
    df_realtime=df_realtime.tail(1)
    print(df_realtime,type(df_realtime))
    make_realtime_graph(df_realtime)
    
    
    frame_no+=1

    out_name=str(frame_no)+".png"
    cv2.imwrite(os.path.join(r"D:\projects\Parking Lot Management system with dashboard\Backend\inferenced_frames",out_name),with_dashboard)
    print("Frames generating!!!")
    cv2.waitKey(10)

