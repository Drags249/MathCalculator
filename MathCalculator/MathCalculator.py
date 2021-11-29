#Import the library for math 
import math


#Euclidean calculator Function that passes in two in values
def EuclideanCalc (x:int,y:int):
    #Use the imported math module to calculate the euclidean and store as the variable eucAnswer
    eucAnswer = math.dist(x,y)
    #return the value eucAnswer to where the function was called 
    return eucAnswer

#Gaussian calculator Function that passes in two in values
def GausCalc (x:int,y:int):
    #Use the imported math module to calculate the gaussian and store as the variable gausAnswer
    
    
    #gausAnswer = MathCalculator. (x,y)
    #return the value gausAnswer to where the function was called
    return gausAnswer

#get the value x from the user 
x = int(input("Please input the first x coordinate number to calculate the euclidean and Gaussian: "))      

#Get the value y from the user 
y = int(input("Please input the second number: "))

#Use the EuclideanCalc function to calculate the Euclidean of x and y
eucAnswer = EuclideanCalc(x,y)

#Use the GausCalc function to calculate the Gaussian of x and y
gausAnswer= GausCalc(x,y)

#Display the answers to the user 
print("The two numbers answered were " + x + " and " + y +".\n The Gaussian is: " + gausAnswer + "\nThe Euclidean is: " + eucAnswer)




