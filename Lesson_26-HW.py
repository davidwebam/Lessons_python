import math


class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Erankyan koxmery petq e linen drakan tver")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Trvats erankyan koxmerov erankyun anhnar e")

        self.a = a
        self.b = b
        self.c = c

    def sides(self):
        return self.a, self.b, self.c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def type_by_sides(self):
        if self.a == self.b == self.c:
            return "Havasarakoxm erankyun"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Havasarasrun erankyun"
        else:
            return "Ankanon erankyun"

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(
            sides[0] ** 2 + sides[1] ** 2,
            sides[2] ** 2
        )

    def angles(self):
        A = math.degrees(math.acos(
            (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
        ))
        B = math.degrees(math.acos(
            (self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)
        ))
        C = 180 - A - B
        return A, B, C

    # Ներգծած շրջանագծի շառավիղ
    def inradius(self):
        return self.area() / (self.perimeter() / 2)

    # Արտագծած շրջանագծի շառավիղ
    def circumradius(self):
        return (self.a * self.b * self.c) / (4 * self.area())
