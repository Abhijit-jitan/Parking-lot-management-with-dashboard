from tkinter import font
import pandas as pd
import matplotlib.pyplot as plt

def realtime_csv_generate(df):
    df_append=pd.DataFrame(df)
    df_append.to_csv(r"D:\projects\Parking Lot Management system with dashboard\Backend\csv\data.csv",mode="a",index=False,header=False)
    print("Data Appended to CSV")


def make_realtime_graph(df):
    """ df will be the csv file from where we are selecting data in tru false format """
    #data_new=pd.DataFrame({"A":[sum(df.sop=="Yes"),sum(df.bottle=="No"),sum(df.gloves=="Yes")],"No":[sum(df.sop=="No"),sum(df.bottle=="Yes"),sum(df.gloves=="No")],},
    index=['A','As','B','C','D']

    #data_new.plot.barh(stacked=True)#, color=["palegreen","mistyrose"])
    plt.bar(df,)

    #fig = plt.figure(figsize=(4,3))
    # Add Title and Labels
    #plt.title('__ Real-Time Activity Graph __')
    plt.yticks([0,1,2,3,4],['Block A','Block A_special','Block B','Block C','Block D'],rotation=45,fontsize=15)
    plt.xlabel('Current State',fontsize=15)
    plt.legend(bbox_to_anchor=(0.9, 1))

    plt.savefig(r"D:\projects\Parking Lot Management system with dashboard\Backend\graph\graph.png")