class BMI:
    def __init__(self,myWeight,myHeight,myName):
        self.myWeight = myWeight
        self.myHeight = myHeight
        self.myName = myName
    def calBMI(self):
        currentBMI = self.myWeight/ (self.myHeight*self.myHeight)
        return currentBMI
    #Test
person = BMI(65,1.8,'john')
print(person.myName,"bmi is",round(person.calBMI(),2))