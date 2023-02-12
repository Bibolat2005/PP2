class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class rectangle(shape):
    def __init__(self,length,wedth):
        super().__init__()
        self.sz=length
        self.cz=wedth
    def area(self):
        return self.sz*self.cz
x=int(input())
y=int(input())
ans=rectangle(x,y)
print(ans.area())
