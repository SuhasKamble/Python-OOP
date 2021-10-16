class Person:
    no_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_no_of_poeple()
        
    @classmethod
    def get_no_of_people(cls):
        return cls.no_of_people

    @classmethod
    def add_no_of_poeple(cls):
        cls.no_of_people += 1

p1 = Person("suhas")
p2 = Person("rohit")
print(Person.get_no_of_people())

        
    
    
        