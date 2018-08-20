
#Define a function that can accept two strings as input and print the string with maximum length in console. If #two strings have the same length, then the function should print al l strings line by line.

#Hints:

#Use len() function to get the length of a string

def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print s1
	elif len2>len1:
		print s2
	else:
		print s1
		print s2
		

printValue("one","three")









    #Minimum 8 characters.
    #The alphabets must be between [a-z]
    #At least one alphabet should be of Upper Case [A-Z]
    #At least 1 number or digit between [0-9].
    #At least 1 character from [ _ or @ or $ ].
    #Input : R@m@_f0rtu9e$
#Output : Valid Password

#Input : Rama_fortune$
#Output : Invalid Password
#Explanation: Number is missing

#Input : Risrael#fortu9e 
#Output : Invalid Password
#Explanation: Must consist from _ or @ or $

import re
password = "R@m@_f0israel9e"
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
 
if flag ==-1:
    print("Not a Valid Password")


