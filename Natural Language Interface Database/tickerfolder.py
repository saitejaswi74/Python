import os
count=0
file=open('ticker.txt','r')

for i in file:
    #print(i)
    x=i.split(":")
    #print(x[1])
    symbol=x[0]
    if(os.path.exists(x[0])):
        print("Directory already exists")
    else:
        os.mkdir(x[0])
        print('Directory Created')
    count+=1
    if(count==6):
        break

