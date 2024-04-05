# Determine the area of intersection of two rectangles where each rectangle 
#is specified by two diagonally opposite input coordinates: lowerleft and topright. 
#Note that some rectangles might not intersect so you have to handle this.
#make the program take inputs on repeat 


import matplotlib.pyplot as plt
import numpy as np
import math

class Area:
    
    def __init__(self, Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
        
        self.Ax1 = Ax1
        self.Ay1 = Ay1
        self.Ax2 = Ax2
        self.Ay2 = Ay2
        self.Bx1 = Bx1
        self.By1 = By1
        self.Bx2 = Bx2
        self.By2 = By2
        self.X_coods = [self.Ax1 , self.Ax2 , self.Bx1 , self.Bx2]
        self.X_coods.sort()
        self.Y_coods = [self.Ay1 , self.Ay2 , self.By1 , self.By2]
        self.Y_coods.sort()
        self.calculate_area()

    def calculate_area(self):

        #checking intersection nd finding area if they do
        if  (Ax1>Bx1 and Ax1> Bx2 and Ax2>Bx1 and Ax2> Bx2) or (Ay1>By2 and Ay1>By1 and Ay2>By2 and Ay2>By1) or (Ax1<Bx1 and Ax1< Bx2 and Ax2<Bx1 and Ax2<Bx2) or (Ay1<By2 and Ay1<By1 and Ay2<By2 and Ay2<By1):
            return ("Rectangles do not intersect")
        else : 
            return(f"Area : {abs(self.X_coods[2]-self.X_coods[1]) * abs (self.Y_coods[2]-self.Y_coods[1])}")
while True : 
    #Input diagnol points
    Ax1 , Ay1 = map(int , input("Enter (x,y) of 1st pt of diagonal of 1st rectangle : ").split())
    Ax2 , Ay2 = map(int , input("Enter (x,y) of 2nd pt of diagonal of 1st rectangle : ").split())
    Bx1 , By1 = map(int , input("Enter (x,y) of 1st pt of diagonal of 2nd rectangle : ").split())
    Bx2 , By2 = map(int , input("Enter (x,y) of 2nd pt of diagonal of 2nd rectangle : ").split())

    #calc area 
    rect1_2 = Area( Ax1 , Ay1 , Ax2 , Ay2 ,Bx1 , By1,Bx2 , By2)
    area = rect1_2.calculate_area()

    #plotting points

    x=[Ax1,Ax2,Bx1,Bx2]
    y=[Ay1,Ay2,By1,By2]

    plt.scatter(x,y)
    plt.plot([Ax1,Ax2] , [Ay1,Ay2],color='black')
    plt.plot([Bx1,Bx2] , [By1,By2],color='black')

    #making rectangles from the points
    a=plt.plot([Ax1,Ax2] , [Ay1,Ay1],color='red' , label ='l')
    b=plt.plot([Ax2,Ax2] , [Ay1,Ay2],color='red' , label='b')
    c=plt.plot([Ax1,Ax2] , [Ay2,Ay2],color='red' , label='l') 
    d=plt.plot([Ax1,Ax1] , [Ay1,Ay2],color='red' ,label='b')

    e=plt.plot([Bx1,Bx2] , [By1,By1],color='blue')
    f=plt.plot([Bx2,Bx2] , [By1,By2],color='blue')
    g=plt.plot([Bx1,Bx2] , [By2,By2],color='blue')
    h=plt.plot([Bx1,Bx1] , [By1,By2],color='blue')

    plt.title(f"Program to find area of intersection \n  {area}")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    #finding area
    rect1_2 = Area( Ax1 , Ay1 , Ax2 , Ay2 ,Bx1 , By1,Bx2 , By2)
    area = rect1_2.calculate_area()

    plt.show()

    choice = input("Do you want to continue (yes/no)? ").lower()
    if choice != 'yes':
        print("Exiting...")
        break


