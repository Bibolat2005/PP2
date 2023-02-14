class person:
    def __init__(self,name,nationality):
        self.name = name
        self.nationality = nationality

    def printinfo(self):  
        print('Name:',self.name)
        print('Nationality:',self.nationality)
    def setSurname(self,surname):
        self.surname = surname
    def getSurname(self):
        return self.surname

class Student(person):
    def __init__(self, name, nationality,id):
        super().__init__(name, nationality)
        self.id = id
    def printinfo(self):
        super().printinfo()
        print('id :',self.id)

class Teacher(person):
    def __init__(self, name, nationality,id):
        super().__init__(name, nationality)
        self.id = id
    def printinfo(self):
        super().printinfo()
        print('id :',self.id)




stud = Student("Bibolat","British","22B030480")
(stud.printinfo())
(stud.setSurname('Kaldybay'))
print(stud.getSurname())
stud1 = Teacher("Arnur","Kazakh","2211515")
(stud1.printinfo())
(stud1.setSurname('Kelgenbaev'))
(stud1.getSurname())