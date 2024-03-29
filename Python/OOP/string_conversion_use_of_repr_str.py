class Car:
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage
    
    # this method is used to describe the class
    # but it not describe when inspect the class
    def __str__(self) -> str:
        return 'a {self.color} car'.format(self = self)
    
    # it will work when inspect
    def __repr__(self) -> str:
        return 'mileage is {self.mileage}'.format(self = self)
    
my_car = Car('red', 12345)
print(my_car) # description
my_car # inspect