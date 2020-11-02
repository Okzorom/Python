#1
def smth(arg1, arg2):
    try:
        arg1, arg2 = float(arg1), float(arg2)
        answer = arg1/arg2
    except ZeroDivisionError:
        return "U can't divide zero"
    return answer
#2
def my_func(**kwargs):
    return kwargs
print(my_func(
    name = input("Name - "),
    surname = input("Surname - "),
    yearofbirth = input("Year of Birth - "),
    city = input("City - "),
    email = input("e-mail - "),
    cell = input("cell number = "),
))
#3
def my_func(ar1, ar2, ar3):
    try:
        mlist = [ar1, ar2, ar3]
        mlist.pop(mlist.index(min(mlist)))
        return sum(mlist)
    except TypeError:
        return "number only"
print(my_func(11, 7, 20))
#4
def mycalc(p_num, n_nam):
    p_num = float(input("Укажите положительное число: "))
    n_nam = float(input("Укажите отрицательное число: "))
    power = p_num ** n_nam
    return power
print(mycalc(10,-5))
#5
def mysum():
    br = False
    result = 0
    while br == False:
        pers_numbers = input("Input some numbers or press q for exit").split()
        res1=0
        for i in pers_numbers:
            if "q" in i:
                br = True
                break
            result += res1
    print(result)

#6
def int_func(word):
    return word.title()

print(int_func("word"))
res_int_func=int_func("text and text again")
print(res_int_func)

