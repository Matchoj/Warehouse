import csv

def number(arg):
    try:
        i = int(arg)
    except:
        raise KeyError
    else:
        print(' Price has been changed sussesfuly !'.center(50))

    return i



class Accesories:
    Editfunc = []
    store=[]
    def __init__(self,name,kind,price,unit,q,promotion):
        self.name = name
        self.kind = kind
        self.price = int(price)
        self.unit = unit
        self.q = int(q)
        self.__promotion = promotion
        Accesories.store.append(self)

    def show(self):
        print("Name = {}".format(self.name))
        print("Kind = {}".format(self.kind))
        print("Price = {}".format(self.price))
        print("Unit = {}".format(self.unit))
        print("Q = {}".format(self.q))
        print("Promotion= {}".format(self.__promotion))

    def set_price(self,price):
        self.price = number(price)
    def set_kind(self,kind):
        self.kind = kind
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def set_q(self,q):
        self.q=q
    def set_unit(self,unit):
        self.unit = unit

    def get_promotion(self):
        return self.__promotion

    def set_prmomotion(self,change):
        if self.kind in inpromo:
            self.__promotion = change

        else:
            print("cannot change status!")

    @classmethod
    def importdata(cls,path):
        with open(path,"w") as file:
            writer= csv.writer(file,delimiter=";",quotechar="'",quoting=csv.QUOTE_MINIMAL)
            #writer.writerow(["Name","Kind","Price","Unit","Qty","Promorion"])
            for c in Accesories.store:
                writer.writerow([c.name,c.kind,c.price,c.unit,c.q,c.__promotion])
        print("Saving sucessful!")

    @classmethod
    def readfromtxt(cls,txt):
        Text2=cls(*txt.split(";"))
        return Text2

    @staticmethod
    def Newitem():
        name=input("name :")
        kind=input("kind :")
        price=input("price :")
        unit=input("unit :")
        q=input("Q-ty :")
        promotin=input("promotin:")
        line=name +';'+kind+';'+price+';'+unit+';'+q+';'+promotin
        return line

    def __delete__(self, instance):
        instance.__delete


    PromoChange = property(get_promotion,set_prmomotion,None)

    Editfunc.append(set_name)
    Editfunc.append(set_kind)
    Editfunc.append(set_price)
    Editfunc.append(set_unit)
    Editfunc.append(set_q)




inpromo = ["Chips"]




