print("Стороны треугольника")
a, b, c = float(input('A=')), float(input('B=')), float(input('C='))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    p = (a + b + c) / 2
    area = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)
    print("Площадь треугольника =", area)
else: print("Треугольник не существует")


