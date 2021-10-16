class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def run():
        print("Run")    

print(Math.add5(2))
print(Math.add(5,5))
Math.run()