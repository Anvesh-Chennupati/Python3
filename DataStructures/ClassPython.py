#Creating a class

class Mammals:
    name = "Homosepians"

    def changename(self,new_name):
        self.name = new_name

human = Mammals()

print(human.name)

human.changename("Birds")
print(human.name)
