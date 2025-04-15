"""
Class that implements variious animal's
mode of movement
"""

class Animal():
    def __init__(self):
        pass

    def move(self):
        print('I am moving!')


class Snake(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        print('Slither')
    
class Dog(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        print('I am walking')


nyoks = Snake()
nyoks.move()


bosco = Dog()
bosco.move()