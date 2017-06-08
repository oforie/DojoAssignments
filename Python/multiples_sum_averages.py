#Multiples part I
for count in range (1, 1001, 2):
    print count

#Multiples part II
for count in range(5, 1000001, 5):
    print count

#sum list
mainList = [1,2,5,10,255,3]
sum = 0
for i in mainList:
    sum +=i
print sum

#Average
mainList = [1,2,5,10,255,3]
sum = 0
for i in mainList:
    sum +=i
average = sum/len(mainList)
print average