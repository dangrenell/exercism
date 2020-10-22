def equilateral(sides):
    return is_a_triangle(sides) and sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides):
    return is_a_triangle(sides) and any([sides[i % 3] == sides[(i + 1) % 3] for i in range(3)])


def scalene(sides):
    return is_a_triangle(sides) and all([sides[i % 3] != sides[(i + 1) % 3] for i in range(3)])


def is_a_triangle(sides):
    return all([sides[i % 3] + sides[(i + 1) % 3] > sides[(i + 2) % 3] for i in range(3)])
