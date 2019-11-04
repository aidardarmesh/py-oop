class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""

class EventGet:
    pass

class EventSet:
    pass

class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor
    
    def handle(self, char, event):
        if self.__successor:
            self.__successor.handle()

class IntHandler:
    pass

class FloatHandler:
    pass

class StrHandler:
    pass

