
# for i in range(2,5):
#     print("square of {0} is {1} and cube of {0} is {2}".format(i,i**2,i**3)) 
#     print("value of pi is {0:12.50}".format(22/7))
while(True):
	num = int(input())
	for i in range(2,num):
	    if (num % i) == 0:
	       print("not prime")
	       break
	else:
	    print("prime")

    
    	
