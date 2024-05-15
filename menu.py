from Store import Accesories
Pa=r"C:\projects\projecccti\file.csv"


def Create():
    txt=Accesories.Newitem()
    item=Accesories.readfromtxt(txt)
    Accesories.importdata(Pa)
def Overview():
    print("{}\t{:20}\t{:20}\t\t\t{:20}".format("Nr.","Name","Kind","Worth"))
    print("--"*33)
    n=1
    for i in Accesories.store:
        print("{}.\t{:20}\t{:20}\t{:13}".format(n,i.name,i.kind,i.price*i.q))
        n+=1
    input("Press any kay to continue :")

def Loading(path):
    texts=[]
    with open(path,"r") as file:
        for line in file:
            nline=line[:-1]
            texts.append(nline)
    ntexts = texts[::2]
    for i in ntexts:
        item= Accesories.readfromtxt(i)

def position():
    x=int(input("Select position : "))
    n= 1
    c=[]
    for i in Accesories.store:
        if x == n:
            c.append(i)
        n+=1
    return c[0]



def Editarg(arg):
    n=1
    for i in Accesories.Editfunc:
        print("{}.\t {}".format(n,i.__name__))
        n+=1
    try:
        choose=int(input("choose arrtibute to change :  "))
    except :
        choose = int(input("Insertet value must be Digit try again :  "))
    finally:
        if choose == 1:
            arg.set_name(input("value : "))
        elif choose == 2:
            arg.set_kind(input("value : "))
        elif choose == 3:
            arg.set_price(input("value : "))
        elif choose == 4:
            arg.set_unit(input("value : "))
        elif choose == 5:
            arg.set_q(input("value : "))
        else:
            print("You have chosen wrong oprion try again")
            Editarg(arg)
    Accesories.importdata(Pa)

def Edit():
    x=position()
    Editarg(x)

def Delete():
    y=position()
    for i in Accesories.store:
        if i == y:
            Accesories.store.remove(i)
            Accesories.importdata(Pa)




def Detailed_info():
    z=position()
    z.show()


def Quit():
    return False


func= []
func.append(Create)
func.append(Overview)
func.append(Detailed_info)
func.append(Edit)
func.append(Delete)
func.append(Quit)



