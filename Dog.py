class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("Barking...")
        
    def running(self):
        print("Running...")
        
d = Dog("Suhas", 20)

print(d.name)
print(d.age)
d.bark()
d.running()
    