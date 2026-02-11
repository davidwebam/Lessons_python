from abc import ABC, abstractmethod
import math

class Animal:
    def eat(self):
        return "Kendanin utum e"

    def sleep(self):
        return "Kendabin qnum e"


class Bird(Animal):
    def eat(self):
        return "Trchuny utum e"

    def fly(self):
        return "Trchuny trnum e"


class Fish(Animal):
    def swim(self):
        return "Dzuky loxum e"

class Shape(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, sharavix):
        if not isinstance(sharavix, (int, float)) or sharavix <= 0:
            raise ValueError("Sharavixy petq e lini drakan tiv")
        self.sharavix = sharavix

    def perimetr(self):
        return 2 * math.pi * self.sharavix

    def area(self):
        return math.pi * self.sharavix ** 2

class Rectangle(Shape):

    def __init__(self, laynutyun, erkarutyun):
        if (not isinstance(laynutyun, (int, float)) or laynutyun <= 0 or
            not isinstance(erkarutyun, (int, float)) or erkarutyun <= 0):
            raise ValueError("Laynutyuny ev erkarutyuny petq e linen drakan tver")
        self.laynutyun = laynutyun
        self.erkarutyun = erkarutyun

    def perimetr(self):
        return 2 * (self.laynutyun + self.erkarutyun)

    def area(self):
        return self.laynutyun * self.erkarutyun

class Triangle(Shape):

    def __init__(self, a=None, b=None, c=None, h=None, alpha=None):
        if a and b and c:
            if a <= 0 or b <= 0 or c <= 0:
                raise ValueError("Koxmery petq e linen drakan")
            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError("Erankyuni kanony xaxtvum e")

            self.a = a
            self.b = b
            self.c = c
            self.mode = 1

        
        elif a and h:
            if a <= 0 or h <= 0:
                raise ValueError("Koghmy ev bardzrutyuny petq e linen drakan")

            self.a = a
            self.h = h
            self.mode = 2

        elif a and b and alpha:
            if a <= 0 or b <= 0 or alpha <= 0:
                raise ValueError("Tvery petq e linen drakan")

            self.a = a
            self.b = b
            self.alpha = alpha
            self.c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(alpha)))
            self.mode = 3

        else:
            raise ValueError("ERROR")

    def perimetr(self):
        if self.mode == 1 or self.mode == 3:
            return self.a + self.b + self.c
        else:
            return "Perimetry chi karox hashvel tvyal parametrerov"

    def area(self):
        if self.mode == 1:
            p = (self.a + self.b + self.c) / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

        elif self.mode == 2:
            return self.a * self.h / 2

        elif self.mode == 3:
            return self.a * self.b * math.sin(math.radians(self.alpha)) / 2
