class calculator:
    def __init__(self):
        self.a = int(input("Enter the first Number: "))
        self.b = int(input("Enter the second Number: "))
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
        
Device_One = calculator()

print('---------------------------------')
print("The Addition of Two Numbers is: ", Device_One.add())
print("The Substraction of Two Numbers is: ", Device_One.sub())