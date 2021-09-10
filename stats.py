import csv
from collections import Counter

with open('weights.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
    file_data.pop(0)
    new_data=[]
    for i in range(len(file_data)):
        n_num=file_data[i][1]
        new_data.append(float(n_num))

m = len(new_data)
total=0

#  mean
for x in new_data :
    total+=x

mean = total/m

#  median
d=len(new_data)
new_data.sort()

if d%2 == 0:
    median1=float(new_data[m//2])
    median2=float(new_data[m//2-1])

    median = (median1+median2)/2
else:
    median=new_data[m//2]
    

# mode
data=Counter(new_data)
mode_data={
    "50-10000":0,
    "10000-15000":0,
    "15000-25000":0
}

for weight,occurence in data.items():
    if 50<float(weight)<10000:
        mode_data["50-10000"] +=occurence
    elif 10000<float(weight)<15000:
        mode_data["10000-15000"] +=occurence
    elif 15000<float(weight)<25000:
        mode_data["15000-25000"] +=occurence

mode_range,mode_occurence=0,0

for range, occurence in mode_data.items():
    if occurence>mode_occurence:
        mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode=float((mode_range[0]+mode_range[1])/2)


print("mean weights = ",mean)
print("median weight = ",median)
print("mode weights =",mode)