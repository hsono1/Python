#function oddEven that prints numbers from 1 to 2000 and specifies whether
#number is odd or even
def oddEven():
    for idx in range(1,2001):
        if idx % 2 == 0:
            print "Number is " +  str(idx) + ". This is an even number"
        else:
            print "Number is " + str(idx) + ". This is an odd number"

oddEven()


#function Multiply that iterates through each value in a= [2,4,10,16]
#and return a list of the new values
def multiply(a,b):
    list1 = []
    for idx in a:
        list1.append(idx * b)
    return list1
        
list2 = [2,4,10,16]
print multiply(list2, 5)


#function layered_multiples() that receives the multiply function as parameter and outputs a multidimensional array with each number converted into 1's

def layered_multiply(array):
    array1 = array
    array2 = []
    array3 = []
    for element in array1:
        array2.append([1] * element)
    print array
    print array1
    print array2



layered_multiply( multiply( [2,4,5], 3) ) 






 




