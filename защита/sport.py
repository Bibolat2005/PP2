class Sportsmen:
    def __init__(self, id, name):
        self.id_ = id
        self.name_ = name
    def printInfo(self):
        print("id of sport is -", self.id_)
        print("name of the sportsman -", self.name_)
    def set_Type(self, type):
        self.type = type
    def get_Type(self):
        print("Type of the sport is: ")
        print(self.type)
    
class TeamSport(Sportsmen):
    def __init__(self, id, name, num_players):
        super().__init__(id, name)
        self.numplayers = num_players
    def printInfoo(self):
        print("Total informations:")
        print(self.id_, self.name_, self.numplayers)

class Football(TeamSport):
    def __init__(self, id, name, num_players, name_team):
        super().__init__(id, name, num_players)
        self.nameteam = name_team
    def printInfooo(self):
        print("Finally INFORMATION:")
        print(self.id_, self.name_, self.numplayers, self.nameteam)


    
    
# y = Sportsmen(7979, "Arnold")
# y.printInfo()
# y.set_Type("football")
# y.get_Type()
# x = TeamSport(7979, "Arnold", 11)
# x.printInfoo()
z = Football(7777, "Bibolat", 11, "Qazaqstan")
z.printInfooo()

