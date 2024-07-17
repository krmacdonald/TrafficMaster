roaddata = [[]]
trafficTypes = ["Road", "Stoplight", "Pedestrian Crossing", "Stop Sign"]
import roads

def printLanes():
    for i in roaddata:
        print(i)

def randomRoadData():
    for i in roaddata:
        for j in i:
            j.Randomize()