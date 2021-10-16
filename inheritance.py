class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old, color is {self.color}")   


class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Suhas",20)
p.show()
c = Cat("Bill", 21, "brown")
c.show()
d = Dog("Jill", 34)
d.show()

