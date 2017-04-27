print "Part1: Printing all numbers from 1 o 1000"
for element in range(1,1001):
    print element

print "Part2: Printing all multiples of 5 from 5 to 1000"
for element in range(5,1001):
    if element % 5 == 0:
        print element
    
print "Part3: Printing the sum of all the values in the list a=[1,2,5,10,255,3]"
a = [1,2,5,10,255,3]
sum = 0
for idx in a:
    sum = sum + idx
print sum

print "Part4: Printing the average of values in previous list"
sum = 0
for idx in a:
    sum = sum + idx
print sum/len(a)       
