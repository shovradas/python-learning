class Data:
    def __init__(self, value):
        self.value = value
 
    # adding two objects 
    def __add__(self, o):
        return self.value + o.value 

obj1 = Data(10)
obj2 = Data(20)
obj3 = Data("String1")
obj4 = Data("String2")

print(obj1 + obj2)
print(obj3 + obj4)
# print(ob1 + ob3) # generates error