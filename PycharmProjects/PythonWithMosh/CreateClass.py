
class Item:
    All = []
    def __init__(self, Name:str, Age:int):
        self.Name = Name
        self.Age = Age

        Item.All.append(self)

    @classmethod
    def printAll(cls):
        print(cls.All)

    def __repr__(self):
        return self.Name

Item1 = Item("Vikas", 31)
Item1 = Item("Alina", 26)
Item.printAll()

