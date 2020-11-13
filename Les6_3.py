class Worker:
    def __init__(self, name, surname, position, dohod):
        self.name = name
        self.surname = surname
        self.position = position
        self._dohod_wage = dohod['wage']
        self._dohod_bonus = dohod['bonus']


class Position(Worker):
    def getfullname(self):
        return f'{self.name} {self.surname} {self.position}'

    def getdohod(self):
        return self._dohod_wage + self._dohod_bonus
pos = Position('Elvira', 'Morozko', 'dreamer', {"wage": 10000000, "bonus": 7000000})
print(pos.getfullname())
print(pos.getdohod())
