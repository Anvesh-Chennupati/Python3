#Creating a class

class Snake:
    def __init__(self,name,length):
        self.name = name
        self.length = length
    def changename(self,new_name):
        self.name = new_name

python = Snake("python",44)
anaconda = Snake("anaconda",55)

print(python.name)
print(python.length)
print(anaconda.name)
print(anaconda.length)
