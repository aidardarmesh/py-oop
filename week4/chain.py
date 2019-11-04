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

class FloatHandler(NullHandler):
    pass

class StrHandler(NullHandler):
    pass

obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
print(chain.handle(obj, EventGet(int)))  # 42
# chain.handle(obj, EventGet(float))
# 3.14
# chain.handle(obj, EventGet(str))
# 'some text'
# chain.handle(obj, EventSet(100))
# chain.handle(obj, EventGet(int))
# 100
# chain.handle(obj, EventSet(0.5))
# chain.handle(obj, EventGet(float))
# 0.5
# chain.handle(obj, EventSet('new text'))
# chain.handle(obj, EventGet(str))
# 'new text'