from os import listdir
from os.path import isfile, join
import pandas as pd
path="../results/"
files = [f for f in listdir(path) if (isfile(join(path, f)) and (".txt" in f))]

data=[]
for fname in files:
    name=fname.split('_')[0]
    length=int(fname.split('_')[-1].replace('.txt',''))
    row=[name,'A',length,1,0.0]
    with open(join(path,fname),"r") as f:
        for line in f.readlines():
            if 'pattern:' in line:
                row[1]=line.replace('pattern: ','').replace('\n','')
            elif 'Found:' in line:
                row[3]=int(line.replace('Found: ','').replace('\n',''))
            elif 'Time:' in line:
                row[4]=float(line.replace('Time: ','').replace(' s','').replace('\n',''))
    data.append(row)

df=pd.DataFrame(data=data,columns=['Algorithm','Pattern','Length','Found','Time'])
df.to_csv('../results/results.csv')