def area(a, b):
    '''
    Возвращает площадь прямоугольника.

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника
            (a и b - смежные стороны)

        Возвращаемое значение:
            area (float): площадь прямоугольника
    '''

    if not(isinstance(a, int)) and not(isinstance(a, float)) or not(isinstance(b, int)) and not(isinstance(b, float)):
        raise TypeError("not number")

    if a < 0 or b < 0:
        raise ValueError("negative number")

    return a * b 

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника.

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника
            (a и b - смежные стороны)

        Возвращаемое значение:
            perimeter (float): периметр прямоугольника
    '''

    if not(isinstance(a, int)) and not(isinstance(a, float)) or not(isinstance(b, int)) and not(isinstance(b, float)):
        raise TypeError("not number")

    if a < 0 or b < 0:
        raise ValueError("negative number")

    return (a + b) * 2 
