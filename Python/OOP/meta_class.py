class Test:
    pass


print(type(Test))  # the type of the class itself is type
print(type(Test()))  # but it's object's type is Test

# we can create the same class in different way!
Test = type('Test', (), {})

# These will give the same output!
print(type(Test))
print(type(Test()))

# Adding attribute using method!


class Person:
    def sayHello(self):
        print('Hello!')


def set_attribute(self):
    self.y = 10


Test2 = type('Test2', (Person,), {'x': 5, 'set_attribute': set_attribute})

obj = Test2()

obj.sayHello()
obj.set_attribute()
print(obj.y)
