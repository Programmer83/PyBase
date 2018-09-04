from math import sqrt

a, b, c = float(input("a > ")), float(input("b > ")), float(input("c > "))

d = b**2 - 4*a*c

if d > 0:
    rts = 2
    x1 = (((-b) + sqrt(d)) / 2 * a)
    x2 = (((-b) + sqrt(d)) / 2 * a)
    print("2 solution : %f and %f" % (x1, x2))
elif d == 0:
    rts = 1
    x = (-b) / 2 * a
    print("1 solution : ", x)
else:
    rts = 0
    print("No sol, the result is a complex value, desc < 0 ")
    exit()