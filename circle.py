import math


def area(r):
    '''
    Возвращает площадь круга.

        Параметр:
            r (float): радиус круга

        Вощвращаемое значение:
            area (float): площадь круга
    '''

    if not(isinstance(r, int)) and not(isinstance(r, float)):
        raise TypeError("not number")

    if r < 0:
        raise ValueError("negative number")

    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметр:
            r (float): радиус круга

        Возвращаемое значение:
            perimeter (float): периметр круга 
    '''

    if not(isinstance(r, int)) and not(isinstance(r, float)):
        raise TypeError("not number")

    if r < 0:
        raise ValueError("negative number")

    return 2 * math.pi * r

