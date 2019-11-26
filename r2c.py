class BMI:
    def __init__(self,myWeight,myHeight,myName):
        self.myWeight = myWeight
        self.myHeight = myHeight
        self.myName = myName
    def calBMI(self):
        currentBMI = self.myWeight/ (self.myHeight*self.myHeight)
        return currentBMI
yourName = input('What is your name?')
yourWeight = float(input('What is your weight in kg?'))
yourHeight = float(input('What is your height in meters?'))
newPerson = BMI(yourWeight,yourHeight,yourName)
newBMI = newPerson.calBMI
print("Dear",newPerson.myName + ", your BMI is",round(newBMI,2))