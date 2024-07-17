import random
class RoadManager:
    def __init__(self):
        self.names = ["Normal", "Stoplight", "Stop Sign", "Pedestrian", "None"]
        self.roadcount = 0
    def RandomName(self):
        return self.names[random.randint(0, 4)]
    def RandomSize(self):
        return random.randint(0, 4)