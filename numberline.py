numberpoint = 0 #variable initialization

while True:
    try:
        numberpoint = int(input("Number of points = " )) #input 
        if isinstance(numberpoint, int): #check if input is an integer
            print()
            break
    except ValueError:
        print("Please Enter A Number Greater Than 1")
if numberpoint == 0: #error case if number is 0
    exit("Please Input A Number Greater Than 1")
if numberpoint < 0: #error case if number less than is 0
    exit("Please Input A Number Greater Than 1")
if numberpoint == 1: #error case if number is 1
    exit("Please Input A Number Greater Than 1")

i = 1 #variable initialization 
pointlist = [] #list initialization

while numberpoint > 0:
    print("Point" , i , "=") 
    while True:
        try:
            pt = int(input()) #ask for value of each point
            if isinstance(pt, int): #Check if number is an integer
                print()             
                break               
        except ValueError:
            exit("Please Enter A Number")
    pointlist.append(pt) #add value given to a list
    numberpoint = numberpoint - 1 #(numberpoint defines how many times the loop runs)
    i = i + 1 # increment i by 1
    
print(pointlist)

print("Calculate distance between two points")

num1 = int(input("Point 1 = ")) #the first point to calculate
if num1 > i: #check if input is an existant point in the list
    exit("This point does not exist")

num2 = int(input("Point 2 = ")) #the second point to calculate
if num2 > i: #check if input is an existant point in the list
    exit("This point does not exist")
    
calc1 = pointlist[num1 - 1] #to compensate as list starts form 0
calc2 = pointlist[num2 - 1] #to compensate as list starts form 0

if calc1 > calc2: #calculation if first point is larger than second point
    print(calc1 - calc2)
if calc2 > calc1: #calculation if second point is greater than first point
    print(calc2 - calc1)
    
    