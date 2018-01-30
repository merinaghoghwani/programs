#the program will enter the last no of digit and a random digit no will be identified
#implement binary search in python

import random
global array

def returnArray(min, max) :
    print "array reduced to %s" %array[min:max]

print "Enter last digit"
lastDigit = input()

array = range(1, lastDigit+1)

randNo = random.choice(array)
count = 0
exit = -1
min = 0
max = lastDigit

while exit!= 0 :
  try :
    count += 1
    print "Guess No. or press 0 to exit"
    exit = input()
    
    if exit == 0 :
      continue
    elif randNo == exit:
      print "Hurray No. matched in %s tries" %count
      exit = 0
    elif randNo > exit :
      min = exit
      returnArray(min, max)
    else:
      max = exit-1
      returnArray(min, max)
    
  except Exception as e :
    print "No. not in the list %s" %e
