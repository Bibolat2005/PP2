
import math

a = int(input())
print(math.radians(a))




#2
import math

h = float(input("Height: "))
b = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))

area = ((b + b2) / 2) * h
print(area)



#3

import math

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(area)





#4
import math

base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

area = base * height

print(area)
