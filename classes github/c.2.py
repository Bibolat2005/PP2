class shape:
    def __init__(self,sz):
        self.sz=sz
    def area(self):
        return 0
class square(shape):
    def __init__(self,sz):
        super().__init__(sz)
        self.sz=sz
    def area(self):
        return self.sz*self.sz
x=int(input())
ans=square(x)
print(ans.area())
