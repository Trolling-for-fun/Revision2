#from 2a
class BMI:
    def __init__(self,myWeight,myHeight,myName):
        self.myWeight = myWeight
        self.myHeight = myHeight
        self.myName = myName
    def calBMI(self):
        currentBMI = self.myWeight/ (self.myHeight*self.myHeight)
        return currentBMI
#from 2b
with open('C:/Users/T05-17/Desktop/listOfNames.txt') as f:
    myArray = f.readlines()
print(myArray)
totalBMI = 0
noOfNames = 0

for lines in myArray:
    myList = lines.split()
    name = myList[0]
    height = float(myList[1])
    weight = int(myList[2])
    person = BMI(weight,height,name)
    myBmi = person.calBMI()
    totalBMI += myBmi
noOfPerson = len(myArray)
averageBMI = totalBMI/noOfPerson
print("Average bmi is",round(averageBMI,2))
#from 2c
yourName = input('What is your name?')
yourWeight = float(input('What is your weight in kg?'))
yourHeight = float(input('What is your height in meters?'))
newPerson = BMI(yourWeight,yourHeight,yourName)
newBMI = newPerson.calBMI()
print("Dear",yourName + ", your BMI is",round(newBMI,2))
#2d
NewAverageBMI = (totalBMI + newBMI) / (noOfPerson +1)
print("New average BMI is",round(averageBMI,2))