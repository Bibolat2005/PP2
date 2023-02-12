class string:
    def __init__(self):
        self.s=''
    def getstring(self):
        self.s=input()
    def printstring(self):
        print(self.s.upper())
ans=string()
ans.getstring()
ans.printstring()