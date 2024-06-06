import os
import datetime
import pandas as pd
import json

import calendar
date = datetime.datetime(2020,1,1)
start_year = 2020
total_days = 1
delta = datetime.timedelta(days=1)

while start_year < 2025 :
    if start_year == 2024 :
        for j in range(1,6):
            summary = []
            os.makedirs(str(start_year)+"/"+str(start_year)+str(j).zfill(2))
            fp = open(str(start_year)+"/"+str(start_year)+str(j).zfill(2)+'/'+'totals.json','w')
            for k in range(1,calendar.monthrange(date.year,date.month)[1]+1) :
                out_frame = pd.DataFrame(columns=['date','resource','value'])
                for file in os.scandir('/home/kilo/playground/task/generated_files') :
                    df = pd.read_csv(str(file.path))
                    df = df.iloc[24*total_days-24:24*total_days]
                    out_frame = pd.concat([out_frame,df],ignore_index=True)
                summary.append({'date':date,'sum':out_frame['value'].sum()})
                filename = str(date.year)+str(date.month).zfill(2)+str(date.day).zfill(2)+'.csv'
                out_frame.to_csv(str(start_year)+"/"+str(start_year)+str(j).zfill(2)+'/'+filename,index=False)
                date += delta
                total_days += 1
            json.dump(summary,fp,indent=6,default=str)
    else :
        for j in range(1,13):
            summary = []
            os.makedirs(str(start_year)+"/"+str(start_year)+str(j).zfill(2))
            fp = open(str(start_year)+"/"+str(start_year)+str(j).zfill(2)+'/'+'totals.json','w')
            for k in range(1,calendar.monthrange(date.year,date.month)[1]+1) :
                out_frame = pd.DataFrame(columns=['date','resource','value'])
                for file in os.scandir('/home/kilo/playground/task/generated_files') :
                    df = pd.read_csv(str(file.path))
                    df = df.iloc[24*total_days-24:24*total_days]
                    out_frame = pd.concat([out_frame,df],ignore_index=True)
                summary.append({'date':date,'sum':out_frame['value'].sum()})
                filename = str(date.year)+str(date.month).zfill(2)+str(date.day).zfill(2)+'.csv'
                out_frame.to_csv(str(start_year)+"/"+str(start_year)+str(j).zfill(2)+'/'+filename,index=False)
                date += delta
                total_days += 1
            json.dump(summary,fp,indent=6,default=str)
    start_year += 1