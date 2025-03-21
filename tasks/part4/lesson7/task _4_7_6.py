class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class StarWithType(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        self._type_star = type_star
        self._radius = radius
        super().__init__(name, massa, temp)


class WhiteDwarf(StarWithType):
    ...


class YellowDwarf(StarWithType):
    ...


class RedGiant(StarWithType):
    ...


class Pulsar(StarWithType):
    ...


stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = filter(lambda star: isinstance(star, WhiteDwarf), stars)

print(*white_dwarfs)