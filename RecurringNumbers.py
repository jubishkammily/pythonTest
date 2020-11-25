import csv


allNumbersMultiArr = [] 

with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        allNumbersMultiArr.append(row) 
       
i = 0
allNumbersMultiArr2 = allNumbersMultiArr
araylenallnumb = len(allNumbersMultiArr)
araeachlen = len(allNumbersMultiArr[0])
mainArrLen = len(allNumbersMultiArr)
# for i in range(len(allNumbersMultiArr)-1):
#     for x in range(araeachlen):
#         #print(x)        
#         if(allNumbersMultiArr[i][x] == allNumbersMultiArr2[i+1][x]):
#             print(allNumbersMultiArr[i][x])

count = 0
for i in range(mainArrLen):
    for j in range(araeachlen):
            #print(allNumbersMultiArr[i][j])
            for k in range(mainArrLen):
                if(i != k):
                    for l in range(araeachlen):
                        if( allNumbersMultiArr[i][j] == allNumbersMultiArr2[k][l]):
                            #print(allNumbersMultiArr2[k][l])                     
                            count = count + 1
                    
   

#print(count)
count = 0
for i in range(mainArrLen):
    for j in range(araeachlen):
            #print(allNumbersMultiArr[i][j])
            for k in range(i+1,mainArrLen):
                if(i != k):
                    for l in range(araeachlen):
                        if( allNumbersMultiArr[i][j] == allNumbersMultiArr2[k][l]):
                            print(allNumbersMultiArr2[k][l])                     
                            count = count + 1


print(count)

print(count)