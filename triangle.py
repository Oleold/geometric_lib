def area(a, h): 
    '''
    Возвращает площадь треугольника.

        Параметры:
            a (float): сторона треугольника
            h (float): высота треугольника

        Возвращаемое значение:
            area (float): площадь треугольника
    '''
    
    if not(isinstance(a, int)) and not(isinstance(a, float)) or not(isinstance(h, int)) and not(isinstance(h, float)):
        raise TypeError("not number")

    if a < 0 or h < 0:
        raise ValueError("negative number")


    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника.

        Параметры:
            a (float): первая сторона треугольника
            b (float): вторая сторона треугольника
            c (float): третья сторона треугольника

        Возвращаемое значение:
            perimeter (float): периметр треугольника
    '''

    if not(isinstance(a, int)) and not(isinstance(a, float)) or not(isinstance(b, int)) and not(isinstance(b, float)) or not(isinstance(c, int)) and not(isinstance(c, float)):
        raise TypeError("not number")

    if a < 0 or b < 0 or c < 0:
        raise ValueError("negative number")

    return a + b + c 
