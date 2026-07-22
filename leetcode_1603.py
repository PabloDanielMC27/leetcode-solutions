# 1603. Design Parking System

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]

    def reduceCar(self, type):
        
        if self.parking[type] > 0:
            self.parking[type] -= 1
            return True
             
        return False

    def addCar(self, carType: int) -> bool:
        return self.reduceCar(carType - 1)
                
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
