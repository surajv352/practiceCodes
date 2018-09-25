for num in range(4):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
       	   print(i)
           if (num % i) == 0:
               break
       else:
           print(num)