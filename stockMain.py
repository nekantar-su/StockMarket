#Nicholas Kantarellis,Dongmin Li
#marketmain.py
#This file will be the main file
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from graphics import *
#importing stock class
from stockClass import Stock
def main():
    intro()
    set()

def intro():
    #will introduce our program
    print("Welcome to our Stock Market prediction where we will take your 5 stocks and determine which stock will have the best value")
    print("We will import the file with a list of stocks in it")
    print("Each stock provides their Expected Return,Risk aversion, and Standard Deviation")


def set():
    readfileName=askopenfilename()
    infile=open(readfileName,'r')#uses r to read file
    #list to hold values of stocks
    lists=[]
    #Looks through file until empty
    for line in infile:
        #split into class
        name,ER,risk,std=line.split(',')
        #adds to list 
        lists.append(Stock(name,ER,risk,std,0))

    #for loop to convert string to int
    for obj in lists:
        obj.ER=float(obj.ER)
        obj.risk=float(obj.risk)
        obj.std=float(obj.std)


    #for loop to calculate each stocks projected U(return)
    for obj in lists:
        #inputs to formula is expected return,risk,standard deviation
        obj.U=calculate(obj.ER,obj.risk,obj.std)
        

#----------------------------GRAPH----------------------------------------------------------
    #Sets initial graph window
    win=GraphWin(width=600,height=600)
    #sets coordinates
    win.setCoords(0.0,0.0,100.0,100.0)
    #Title of graph
    title=Text(Point(45.0,95.0),"Market Prediction")
    title.draw(win)
    underline=Line(Point(35.0,94.0),Point(56.0,94.0))
    underline.draw(win)
    yaxis=Line(Point(20.0,25.0),Point(20.0,77.0))
    yaxis.draw(win)
    xaxis=Line(Point(20.0,25.0),Point(75.0,25.0))
    xaxis.draw(win)
    #Xaxis label
    xlabel=Text(Point(45.0,10.0),"STOCKS")
    xlabel.draw(win)
    #Yaxis label
    ylabel=Text(Point(10.0,50.0),"U-VALUE")
    ylabel.draw(win)
    #Yaxis labels
    y1=Text(Point(19.0,25.0),"0")
    y1.draw(win)
    y2=Text(Point(19.0,35.0),"1")
    y2.draw(win)
    y3=Text(Point(19.0,45.0),"2")
    y3.draw(win)
    y3=Text(Point(19.0,55.0),"3")
    y3.draw(win)
    y4=Text(Point(19.0,65.0),"4")
    y4.draw(win)
    y5=Text(Point(19.0,75.0),"5")
    y5.draw(win)
    #Xaxis label
    x1=Text(Point(25.0,22.0),lists[0].name)
    x1.draw(win)
    #Size of bar 1
    s0=sizebar(lists[0].U)
    rec1=Rectangle(Point(22.0,25.0),Point(28.0,s0))
    rec1.setFill("Red")
    rec1.draw(win)
    x2=Text(Point(36.0,22.0),lists[1].name)
    x2.draw(win)
    #Size of bar2
    s1=sizebar(lists[1].U)
    rec2=Rectangle(Point(33.0,25.0),Point(39.0,s1))
    rec2.setFill("Blue")
    rec2.draw(win)
    x3=Text(Point(47.0,22.0),lists[2].name)
    x3.draw(win)
    #Size of bar 3
    s2=sizebar(lists[2].U)
    rec3=Rectangle(Point(44.0,25.0),Point(50.0,s2))
    rec3.setFill("Orange")
    rec3.draw(win)
    x4=Text(Point(58.0,22.0),lists[3].name)
    x4.draw(win)
    #Size of bar 4
    s3=sizebar(lists[3].U)
    rec4=Rectangle(Point(55.0,25.0),Point(61.0,s3))
    rec4.setFill("Black")
    rec4.draw(win)
    x5=Text(Point(69.0,22.0),lists[4].name)
    x5.draw(win)
    #Size of bar 5
    s4=sizebar(lists[4].U)
    rec5=Rectangle(Point(66.0,25.0),Point(72.0,s4))
    rec5.setFill("Green")
    rec5.draw(win)
    win.getMouse()
    win.close()
    conclusion()
    

        

def calculate(ER,risk,std):
    #formula to calculatte u: U=E(r)-1/2A STD^2
    U=(ER-(1/2 * risk *(std*std))*-1)
    return U

def sizebar(U):
    #determine size of bar
    x=0.0
    if(U<0.25):
        x=35.0
        return x
    elif ((U<0.50)&(U>0.25)):
        x=45.0
        return x
    elif ((U<0.75)&(U>0.50)):
        x=55.0
        return x
    elif ((U<1.00)&(U>0.75)):
        x=65.0
        return x
    elif ((U>1.00)):
        x=75.0
        return x
    

def conclusion():
    print()
    print("As you can see from the previous graph stock Google has the highest potential")
    print("Thank you for using our predictor. Come again")

#def highestU():
    


main()   
