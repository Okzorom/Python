from math import factorial
from itertools import count

def s_num():
    for i in count(1):
        yield factorial(i)

y=0
for o in s_num():
    print("factorial {} - {} ".format(y+1,o))
    if y==15:
        break
    y +=1
