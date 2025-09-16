import time 

seconds = time.time() 

hours = int(seconds//3600) 

minutes = int((seconds//60)%60) 



print("Hours is: ",hours,"\nMinutes is: ",minutes)