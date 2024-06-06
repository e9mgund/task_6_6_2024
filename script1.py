import pandas as pd
import os
import datetime

import random

for i in range(1,6543):
    file = []
    resource = chr(random.randrange(65,90)) + "".join([chr(random.randrange(97,122)) for j in range(15)])
    start = datetime.datetime(year=2020,month=1,day=1,hour=0)
    end = datetime.datetime(year=2024,month=5,day=31,hour=23)
    delta = datetime.timedelta(hours=1)
    while start <= end :
        value = round(random.uniform(20.00,142.00),2)
        file.append({'date':start,'resource':resource,'value':value})
        start += delta
    df = pd.DataFrame(file)
    df.to_csv(f'generated_files/{i}.csv')