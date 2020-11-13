class road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def rasch(self):
        raschet = self._width*self._length*25*5
        return raschet
road_raschet = road(100,31)
print(road_raschet.rasch())
