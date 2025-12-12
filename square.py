
def area(a):
    '''
    Возвращает площадь квадрата.

        Параметр:
            a (float): сторона квадрата

        Возвращаемое значение:
            area (float): площадь квадрата
    '''

    if not(isinstance(a, int)) and not(isinstance(a, float)):
        raise TypeError("not number")

    if a < 0:
        raise ValueError("negative number")

    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата.

        Параметр:
            a (float): сторона квадрата

        Возвращаемое значение:
            perimeter (float): периметр квадрата
    '''

    if not(isinstance(a, int)) and not(isinstance(a, float)):
        raise TypeError("not number")

    if a < 0:
        raise ValueError("negative number")
    
    return 4 * a
