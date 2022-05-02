import pandas as pd
import numpy as np

data = pd.read_csv("data.txt",header=None)
seat_id = []

for i in data.values:
    for j in i:
        row = np.arange(start=0,stop=128)
        collumn = np.arange(start=0,stop=8)
        for k in j:
            if k == 'F':
                row = row[:round(row.__len__()/2)]
            elif k == 'B':
                row = row[round(row.__len__()/2):]
            if k == 'R':
                collumn = collumn[round(collumn.__len__()/2):]
            elif k == 'L':
                collumn = collumn[:round(collumn.__len__()/2)]

        seat_id.insert(seat_id.__len__(),row[0]*8+collumn[0])
seat_id.sort()
arr = np.arange(start=seat_id[0],stop=seat_id[seat_id.__len__()-1]+1)
print(seat_id[seat_id.__len__()-1])
for i,j in zip(seat_id,arr):
    if i != j:
        print(j)
        break