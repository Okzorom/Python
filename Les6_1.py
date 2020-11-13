import itertools

class TrafficLight:
    def __init__(self):
        self.__color = (('red', 5), ('yellow', 2), ('green', 28))
    def running(self):
        for color, seconds in itertools.cycle(self.__color):
            print(color, '`(U needa wait {} seconds'.format(seconds))
trafficlight = TrafficLight()

trafficlight.running()

