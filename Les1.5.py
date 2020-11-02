rev = int(input('Введите значение выручки: '))
exp = int(input('Введите значение издержек: '))
netprof = int(rev-exp)
if netprof == 0:
    print('Вы сработали в ноль')
if netprof > 0:
    print('Ваш доход составил ', netprof, ' usd, а рентабельность составила ', (rev-exp)/rev*100, '%')
    num = int(input('Сколько сотрудников работает в компании? '))
    print(f'Доход на одного сотрудника составил {(rev - exp) / num} usd')
if netprof < 0:
    print("ваш убыток ", netprof, " usd")
