class Computer:
    ram = 2

    def configuration(value):
        print("i5")
        print(value.ram)

    # Static method
    def welcome_message():
        print("Computer is running.....")


c1 = Computer()

"""
object.method() == class_name.method(object)
that's why we should have at least one argument in the method
unless it will give error like-
method takes 0 positional argument but 1 given!
"""
Computer.configuration(c1)

'''
If we want use method without any attachment with any object
it's known as static method then we need to invoke it from class directly
'''

Computer.welcome_message()
