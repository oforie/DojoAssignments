def odd_even():
    for count in range(0, 2001):
        if count % 2 == 0:
            print "Number is", count,".", "This number is even"
        else:
            print  "Number is", count, "This number is odd"
odd_even()



#Multiply assignment

def multiply(arr, num):


    for x in range(len(arr)):
       arr[x]= arr[x]*num
    return arr

a = [2,4,10,16]
b = multiply(a,5)

print b