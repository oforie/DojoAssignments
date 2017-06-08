#Create a function that when given a list
#identifies a data type and prints specified message
#if a number, adds to a running sum
# if a string, concatenates to another string


list2 = ['magical unicorns', 19, 'hello', 98.98, 'world']

def data_type(li):
    tally = 0
    type_count = 0
    new_string = "I am stringy, get it?"
    for val in li:
        if type(val) == int:
            tally = tally+val
            type_count = type_count + 1
        if type(val)== float:
            tally = tally+val
        if type(val) == str:
            type_count = type_count + 1
            print val, ":", new_string
    
    if type_count > 1:
        print "This list is composed of mixed data types." "There are", type_count, "data types"
        
    print "This is a tally of all numbers in our list", tally
data_type(list2)
            