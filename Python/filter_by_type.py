#Create a list from the evalamples given: (li)

#Create a function with the list as a parameter:

list_1 = [20, 100, 700, "yellow", "Benjamin",[2, 4, 6, 8],4000]

def filterByType(li):
    for val in li:
        if isinstance(val, int):
            if val >= 100:
                print "That's a big number"
            else:
                print "Thats a small number"

        elif isinstance(val, str):
            if len(val) >= 50:
                print "Long sentence"
            else:
                print "Short sentence"

        elif isinstance(val, list):
            if len(val) >= 100:
                print "Big list"
            else:
                print "Short list"

filterByType(list_1)