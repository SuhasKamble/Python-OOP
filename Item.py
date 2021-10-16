import csv

class Item:
    pay_rate = 0.8 # The pay rate afer 20% discount
    all = []
    def __init__(self, name:str, price: float, quantity=0):

        # run validations to the recieved arguments
        assert price >= 0 , f"Price {price} is not greater than or equal to zero!"

        assert quantity >= 0  , f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        print("You are trying to get")
        return self.__name  

    @name.setter
    def name(self, value):
        print("you are trying to set")
        self.__name = value 

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate 

    @staticmethod
    def is_interger(num):
        if isinstance(num, int):
            return True
        elif isinstance(num, float):
            return num.is_integer()
        else:
            return False     
        

    @classmethod
    def instantiate_from_csv(cls):

        with open('main.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )
            
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
 
