#1
Name = input("enter Ur name")
Year = int(input("enter Ur age"))
print("Hi, I'm ", Name, ", i'm", Year)
#2
time_sec = int(input('please input a time: '))
hours = time_sec // 3600
minuts = (time_sec // 60) - (hours * 60)
seconds = time_sec % 60
print(hours, ':', minuts, ':', seconds)

#3
n = input('input n:')
nn = int(n+n)
nnn = int(n+n+n)
int_n = int(n)
final = int_n + nn + nnn
print ('Final = ', final)
#4
l = int(input('Please input integer'))
max = 0
while l> 0:
    mod = l % 10
    if mod > max:
        max = mod
    l = l // 10
print("Max is ", max)
