import pandas as pd

df = pd.read_excel(r'C:\Users\b.todorov\Desktop\a710.xlsx')
filt = df['Storage Bin'].str[-1] == '0'
result = df[filt]
result.to_excel('A710_0.xlsx')
