import os
import datetime
import pandas as pd
import json
import calendar

out_dir = 'processed'
os.mkdir(out_dir)

#path for the generated files in the first task
gen_path = '/home/kilo/playground/task/generated_files'

for file in os.scandir(gen_path):
    fp = open(file.path)
    data = fp.readlines()
    resource_name = data[1].strip().split(',')[1]
    start_date = datetime.datetime(year=2020,month=1,day=1)
    end_date = datetime.datetime(year=2024,month=5,day=31,hour=23)
    delta = datetime.timedelta(days=1)
    totals = []
    for i in range(1,len(data),24):
        dir_path = os.path.join(out_dir,resource_name,str(start_date.year),str(start_date.year)+str(start_date.month).zfill(2))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(os.path.join(dir_path,str(start_date.year)+str(start_date.month).zfill(2)+str(start_date.day).zfill(2)+'.csv'),'w') as out :
            out.write('date,resource,value\n')
            out.writelines(data[i:i+24])
            day_sum = sum([float(i.strip().split(',')[-1]) for i in data[i:i+24]])
            totals.append({'date':start_date,'sum':day_sum})
        if start_date.day == calendar.monthrange(start_date.year,start_date.month)[1] :
            with open(os.path.join(dir_path,'totals.json'),'w') as jp:
                json.dump(totals,jp,indent=6,default=str)
            totals = []
        start_date += delta
    fp.close()