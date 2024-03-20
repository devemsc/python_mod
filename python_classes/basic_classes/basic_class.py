class vehicleDetails:
    def __init__(self):
        self.price=int(input("Enter the Price: "))
        self.model=input("Enter the Model of vehiclee: ")
        
    def GetPrice(self):
        print("The Price of the vehicle is: ", self.price)
    def GetModel(self):
        print("The Model of the vehicle is:", self.model)

obj = vehicleDetails()

obj.GetPrice()

        