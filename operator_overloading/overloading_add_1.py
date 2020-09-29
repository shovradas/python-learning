class Data:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
 
    # adding two objects 
    def __add__(self, o):
        return self.value1 + o.value1, self.value2 + o.value2

obj1 = Data(10, 20)
obj2 = Data(-10, -20)
obj3 = Data("String1.1", "String1.2")
obj4 = Data("String2.1", "String2.2")

print(obj1 + obj2)
print(obj3 + obj4)