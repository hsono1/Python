#function that tosses a coin 5000 times and display
#whether its head or tail and count the times for each

import math
import random

HEAD = 1
TAIL = 0

def coinToss(num):
    sumHead = 0
    sumTail = 0
    for idx in range(1, num + 1):
        var1 = math.floor(random.random()*2)
        if var1 == HEAD:
            sumHead += 1    
            str =  "Attempt #" +  str(idx) + ":throwing a coin... It's is head! ... Got "
            str += str(sumHead) + "head(s) so far and" + str(sumTail) + "tail(s) so far"
            print str
        else:
            sumTail += 1
            str =  "Attempt #", idx, ":throwing a coin... It's is tail! ... Got ", sumHead
            str += "head(s) so far and", sumTail, "tail(s) so far"
            print str


coinToss(10)
        
