class Person:
    def __init__(self, name=None, age=None):
        self._name = name
        self._age = age
    
    def greet(self):
        print(f"Hello, my name is {self._name} and I am {self._age} years old.") 




man1 = Person("Max Payne1", 37)
man1.greet()
