import random

def coin_toss(rep):
    print "Starting the Program"

    headcount = 0
    tailcount = 0 
    counter = 0
    result = ""

    for x in range(0, rep):
        score =random.randint(0,1)
        
        if score == 0:
            result = "Head!"
            headcount += 1
            print "Attempt #",counter,": it's a",result,"Got",headcount,"head(s) so far and",tailcount, "tails so far"
        else:
            result = "Tail!"
            tailcount += 1
            print "Attempt #",counter,": it's a",result,"Got",headcount,"head(s) so far and",tailcount, "tails so far"
        counter += 1

    print "Game Over, thanks for playing!"
coin_toss(5000)