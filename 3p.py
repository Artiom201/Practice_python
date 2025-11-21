from math import sqrt
#1
n = int(input())
h = n // 60
m = n - (h * 60)
print(f"{h} часов и {m} минут")
#2
a = int(input())
b = int(input())
h = int(input())
if  a <= h <= b:
    print("НОРМАЛЬНО")
elif h < a:
    print("НЕДОСЫП")
else:
    print("ПЕРЕСЫП")
# #3

a = int(input())
b = int(input())
c = int(input())
ps =(a + b + c) / 2
s = sqrt(ps * ((ps - a) * (ps - b) * (ps - c)))
print(s)

#4

type = input("Введите тип фигуры комнаты: ")
if type == "Треугольник":
    a = int(input("Введите сторорну А: "))
    b = int(input("Введите сторорну В: "))
    c = int(input("Введите сторорну С: "))
    ps = (a + b + c) / 2
    s = sqrt(ps * ((ps - a) * (ps - b) * (ps - c)))
    print("Площадь данной комнаты:",s)
elif type == "Прямоугольник":
    a = int(input("Введите сторорну А: "))
    b = int(input("Введите сторорну В: "))
    print("Площадь данной комнаты:", a * b)
elif type == "Круг":
    r = int(input("Введите радиус: "))
    print("Площадь данной комнаты:", 3.14 * (r ** 2))

#5

n = int(input())
h = n % 10
if h == 0 or  h == 5 or  h == 6 or h == 7 or h == 8 or h == 9:
    print(n, "программистов")
elif h == 1:
    print(n, "Програмист")
elif h == 2 or h == 3 or h == 4:
    print(n, "Програмиста")
    
#6
n = int(input())
n1 = n // 100000
n2 = n // 10000 % 10
n3 = n // 1000 % 10
n4 = n // 100 % 10
n5 = n // 10 % 10
n6 = n % 10
if (n1 + n2 + n3)   == (n4 + n5 + n6):
    print("Билет счастливый")
else:
    print("билет не счастливый")

    