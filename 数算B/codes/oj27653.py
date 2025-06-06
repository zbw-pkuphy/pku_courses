import math
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        gcd0=math.gcd(abs(numerator),abs(denominator))
        self.numerator //= gcd0
        self.denominator //= gcd0
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
n1,m1,n2,m2 = map(int,input().split())
f1 = Fraction(n1,m1)
f2 = Fraction(n2,m2)
print(f1+f2)