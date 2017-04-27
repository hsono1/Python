#dictionary assignments

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def displayDict(arr):
	for element in arr:
		str1 = ''
		sum = 0
       		for val in element.values():
			str1 += val + " "
			sum = sum + len(val)
		print str1 + str(sum)


		



# displayDict(students)   
print "\n"


#Part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

def displayDict2(arr):
	for key, data in arr.items():
		print key
		displayDict(data)




displayDict2(users)    