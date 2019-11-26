class BMI:
    def __init__(self,myWeight,myHeight,myName):
        self.myWeight = myWeight
        self.myHeight = myHeight
        self.myName = myName
    def calBMI(self):
        currentBMI = self.myWeight/ (self.myHeight*self.myHeight)
        return currentBMI

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
noOfPerson = len (myArray)
averageBMI = totalBMI/noOfPerson
print("Average bmi is",round(averageBMI,2))
    #Test
    #print(name,'has h is',height, 'w is',weight)
    #print(name,height,weight)