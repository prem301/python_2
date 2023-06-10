print ("The Prime Numbers in the range 3 to 30  ") 
for i in range (2, 31): 
 for j in range (2, i): 
  if (i % j) == 0: 
   break 
 else: 
      print (i, end = " ")