import math
def f(x):
    return (x**3- 5* (x**2)+ 10*x - 80)
def df(x):
    return (3*x**2 - 10*x + 10)
x=0
while abs(f(x))>10**(-11):
    x=x-f(x)/df(x)
print(f"{x:.9f}")