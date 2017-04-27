str = "If monkeys like bananas, then I must be a monkey!"
print str.find('monkey')
var1 = str.find('monkey') + 1
print str.find('monkey',var1)


str2 = str
print str2.replace('monkey', 'alligator')

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
y = [x[0], x[len(x)-1]]
print y

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = [x[0], x[1]]
print y
x.remove(-2)
x.remove(-3)
x.insert(0, y)
print x








