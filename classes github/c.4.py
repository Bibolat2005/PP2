import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def chage(self,x,y):
        self.x+=x
        self.y+=y
    def dist(self,a,b):
        print(math.sqrt(a-self.x)**2+(b-self.y)**2)
x=int(input())
y=int(input())
z=int(input())
t=int(input())
a=int(input())
b=int(input())
ans=Point(x,y)
ans.show()
ans.chage(z,t)
ans.dist(a,b)
