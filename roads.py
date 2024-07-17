import roadmanager
import random
manager = roadmanager.RoadManager()
class Road:
    def __init__(self):
        self.name = ""
        self.size = 1
        self.canDrive = False
        self.oneWay = False
    
    
    def Randomize(self):
        self.name = manager.RandomName()
        self.size = manager.RandomSize()
        if(self.name == "Normal" or self.name == "Stoplight" or self.name == "Stop Sign" or self.name == "Pedestrian"):
            self.canDrive = True
        else:
            self.canDrive = False
        
        if(random.randint(0, 1) == 0):
            self.oneWay = True
        else:
            self.oneWay = False
    
    def SetParameters(self, name, size, oneWay):
        self.name = name
        self.size = size
        if(self.name == "Normal" or self.name == "Stoplight" or self.name == "Stop Sign" or self.name == "Pedestrian"):
            self.canDrive = True
        else:
            self.canDrive = False
        self.oneWay = oneWay
