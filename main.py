from menu import func,Pa,Loading
import os

# Loading Data
Loading(Pa)

# Displaying Manu
def Display():
    n=1
    line="*"*40
    print("\n")
    print("{:15} {}".format("",line))
    for i in func:
        print("{:30}.  {}".format(n,i.__name__))
        n+=1
    print("{:15} {}".format("",line))
    print("\n")

# Function is returning choice of user
def Choose():
    try:
        choice=int(input("Command : "))
        if choice in range(len(func)+1):
            print(choice)
        else:
            print("Choose number from the list above")
            Choose()
    except:
        print("Value must be digit.")
        Choose()
    return choice-1

# This function will generate one of the functions in list func
def Answer(arg):
    x=func[arg]
    return x

# Main loop
Con = True
while Con:
    os.system("cls")
    Display()
    a1=Choose()
    a2=Answer(a1)
    a2()
    if a1 == 5:
        Con = a2()
