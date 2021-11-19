"""
File: bouncywithgui.py
Project 8.2

Determines the distance traveled by a bouncing ball.

Inputs: Initial height, bounciness index, and number of bounces
"""
from breezypythongui import EasyFrame

def computeDistance(height, index, bounces):
    distance = 0.0

    for eachPass in range(bounces):
        distance += height
        height *= index
        distance += height
    
    return distance

class BouncyGUI(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self,  title="Bouncy")
        
        self.addLabel(text="Initial height", row = 0, column = 0)
        self.heightField = self.addFloatField(value="", row = 0, column = 1)

        self.addLabel(text="Bounciness index", row = 1, column = 0)
        self.indexField = self.addFloatField(value="", row = 1, column = 1)

        self.addLabel(text="Number of bounces", row = 2, column = 0)
        self.bouncesField = self.addIntegerField(value="", row = 2, column = 1)

        self.addButton(text="Compute", row = 3, column = 1, command=self.computeDistance)

        self.addLabel(text="Total distance", row = 4, column = 0)
        self.distanceField = self.addFloatField(value="", row = 4, column = 1)

    def computeDistance(self):
        height = self.heightField.getNumber()
        bounces = self.bouncesField.getNumber()
        index = self.indexField.getNumber()
        
        results = computeDistance(height, index, bounces)
        
        self.distanceField.setNumber(results)

def main():
    BouncyGUI().mainloop()

if __name__ == "__main__":
    main()
