class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""

class EventGet:
    def __init__(self, type_):
        self.type = type_

class EventSet:
    pass

class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor
    
    def handle(self, char, event):
        if self.__successor:
            self.__successor.handle()

class IntHandler(NullHandler):
    def handle(self, char, event):
        if event.type is int:
            return char.integer_field
        else:
            super().handle(char, event)

class FloatHandler:
    pass

class StrHandler:
    pass

