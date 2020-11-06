from sys import argv
vyrabotka_chas, stavka_chas, premiya = map(float, argv[1:])
print('Payment {} '.format(vyrabotka_chas * stavka_chas + premiya))