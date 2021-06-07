import os 
import pandas as pd
cwd = os.path.abspath('')
files = os.listdir(cwd)

files = files[:len(files) - 1]

df = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        df = df.append(pd.read_csv(file), ignore_index=True) 
df.head() 
df.to_excel('total_sales.xlsx')