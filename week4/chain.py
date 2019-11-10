class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""

class EventGet:
    def __init__(self, type_):
        self.type = type_

class EventSet:
    def __init__(self, value):
        self.value = value
        self.type = type(value)

class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor
    
    def handle(self, char, event):
        if self.__successor:
            return self.__successor.handle(char, event)

class IntHandler(NullHandler):
    def handle(self, char, event):
        if event.type is int:
            if isinstance(event, EventGet):
                return char.integer_field
            else:
                char.integer_field = event.value
        else:
            return super().handle(char, event)

class FloatHandler(NullHandler):
    def handle(self, char, event):
        if event.type is float:
            if isinstance(event, EventGet):
                return char.float_field
            else:
                char.float_field = event.value
        else:
            return super().handle(char, event)

class StrHandler(NullHandler):
    def handle(self, char, event):
        if event.type is str:
            if isinstance(event, EventGet):
                return char.string_field
            else:
                char.string_field = event.value
        else:
            return super().handle(char, event)
