class animal(object):
    def __init__(self, startname,age):
        self.name = startname # attribute
        self.age = age #attribute2
    def description(self): #method1
        print("This is " + self.name)
        print("He/She is " + str(self.age)+" years old! HUBA HUBA")
