def equilateral(sides):
    """
    This function takes in the sides and checks whether it is an equilateral or not

    :param sides: List of three sides of a potential triangle
    :return: bool value, True if the triangle qualifies to be an equilateral triangle
    """
    is_equilateral = False
    a, b, c = sides
    if is_sides(a, b, c):
        if is_triangle_property(a, b, c):
            if a == b == c:
                is_equilateral = True
    else:
        is_equilateral = False

    return is_equilateral


def isosceles(sides):
    """
    This function takes in the sides and checks whether it is an isosceles triangle or not

    :param sides: List of three sides of a potential triangle
    :return: bool value, True if the triangle qualifies to be an iscoscleles triangle
    """

    a, b, c = sides
    is_isosceles = False

    if is_sides(a, b, c):
        if is_triangle_property(a, b, c):
            if equilateral(sides) or (a == b) or (a == c) or (b == c):
                is_isosceles = True
    else:
        is_isosceles = False

    return is_isosceles


def scalene(sides):
    """
    This function takes in the sides and checks whether it is an Scalene triangle or not

    :param sides: List of three sides of a potential triangle
    :return: bool value, True if the triangle qualifies to be an Scalene triangle
    """
    a,b,c = sides
    if equilateral(sides) or isosceles(sides):
        return False
    else:
        if is_sides(a,b,c) and is_triangle_property(a,b,c):
            return True
        else:
            return False


def is_sides(a, b, c):
    """
    This function takes in the sides and checks the sides are non zero

    :param a, b, c: the three sides of the triangle
    :return: bool value, True if the triangle qualifies to be a triangle
    """

    is_sides = False
    if (a * b * c) == 0:
        is_sides = False
    else:
        is_sides = True
    return is_sides


def is_triangle_property(a, b, c):
    """
    This functions makes sure the three values passed as triangle sides satisfy the triangle inequality
    :param a, b, c: The three sides of the triangle
    :return:
    """
    is_triangle_property = False
    if (a + b) >= c:
        if (a + c) >= b:
            if b + c >= a:
                is_triangle_property = True

    return is_triangle_property



