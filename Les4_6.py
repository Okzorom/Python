def generator():
    i=3
    while i < 10:
        i +=1
        yield i
gen_obj = generator()
for num in gen_obj:
    print(num)
from itertools import cycle
x = [1, True, "sth serious", 5, 11, 5]
for i in enumerate(cycle(x)):
    print(x)
    if i == 5:
        break
