
demoList = []

for i in range(0,3,1):
    a=int(input("Enter number: "))
    demoList.insert(i,a)

print(demoList)


sum=0
for i in demoList:
    sum=sum+i

print(sum/len(demoList))
