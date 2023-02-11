import math
def volume(r):
    v=(4/3)*math.pi*(pow(r,3))
    return v
r=int(input())
print(volume(r))