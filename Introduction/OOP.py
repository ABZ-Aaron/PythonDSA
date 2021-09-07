

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        integer = self.is_integer(self.num, self.den)

        if not integer:
            raise Exception ("Not an integer")

        common = self.gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def is_integer(self, n, d):
        return (isinstance(n, int) and isinstance(d, int))

    def __sub__(self, other_fraction):

        new_num = self.num * other_fraction.den \
        - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = self.gcd(new_num, new_den)
        return Fraction(new_num, new_den)

    def __lt__(self, other_fraction):
        div = self.num / self.den
        div_2 = other_fraction.num / other_fraction.den

        return (div < div_2)

    def __mul__(self, other_function):
        new_num = self.num * other_function.num
        new_den = self.den * other_function.den

        return Fraction(new_num, new_den)

    def __truediv__(self, other_function):
        new_num = self.num * other_function.num
        new_den = self.den * other_function.num

    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

x = Fraction(1.2, 2)
#y = Fraction(2, 3)
#z = Fraction(4, 8)


x.show()


