from colour import bcolors

class Burger():
    def __init__(self,name,patty,price,input):
        self.name  = name
        self.patty = patty
        self.price = price
        self.input = input
    def toString(self):
        pburg_det =(bcolors.red+"### {0} ###\n"
                       .format(self.name)+
                       bcolors.black+"Patty  :{0}\n"
                       .format(self.patty)+
                       "Price  :"+bcolors.green+"${0}\n"
                       .format(self.price)+bcolors.red+
                       "Input  :"+bcolors.blue+"[{0}]"
                       .format(self.input)+bcolors.black)
        print(pburg_det)

class Cheeseburger(Burger):
    def __init__(self,name,patty,cheese,price,input):
        Burger.__init__(self,name,patty,price,input)
        self.cheese=cheese
    def toString(self):
        cheburg_det =(bcolors.red+"### {0} ###\n"
                       .format(self.name)+
                       bcolors.black+"Layers :{0} and {1}\n"
                       .format(self.patty,self.cheese)+
                       "Price  :"+bcolors.green+"${0}\n"
                       .format(self.price)+bcolors.red+
                       "Input  :"+bcolors.blue+"[{0}]"
                       .format(self.input)+bcolors.black)
        print(cheburg_det)

class Compburger(Cheeseburger):
    def __init__(self,name,patty,cheese,vegetable,price,input):
        Cheeseburger.__init__(self,name,patty,cheese,price,input)
        self.veg   = vegetable
    def toString(self):
        comburg_det = (bcolors.red + "### {0} ###\n"
                        .format(self.name) +
                        bcolors.black + "Layers :{0}, {1} and {2}\n"
                        .format(self.patty, self.cheese,self.veg) +
                        "Price  :" + bcolors.green + "${0}\n"
                        .format(self.price) + bcolors.red +
                        "Input  :" + bcolors.blue + "[{0}]"
                        .format(self.input)+bcolors.black)
        print(comburg_det)

class Doubcheburg(Cheeseburger):
    def __init__(self,name,patty,cheese,patty2,cheese2,price,input):
        Cheeseburger.__init__(self,name,patty,cheese,price,input)
        self.patty2 = patty2
        self.cheese2= cheese2
    def toString(self):
        dcheburg_det =(bcolors.red+"### {0} ###\n"
                       .format(self.name)+
                       bcolors.black+"Layers :{0} and {1}\n"
                       .format(self.patty,self.cheese)+
                       "Price  :"+bcolors.green+"${0}\n"
                       .format(self.price)+bcolors.red+
                       "Input  :"+bcolors.blue+"[{0}]"
                       .format(self.input)+bcolors.black)
        print(dcheburg_det)

class Sidecourse():
    def __init__(self,name,price,input):
        self.name   = name
        self.price  = float(price)
        self.input  = input
    def toString(self):
        scourse_det =(bcolors.red+"### {0} ###\n"
                       .format(self.name)+
                       "Price  :"+bcolors.green+"${0}\n"
                       .format(self.price)+bcolors.red+
                       "Input  :"+bcolors.blue+"[{0}]"
                       .format(self.input)+bcolors.black)
        print(scourse_det)

class Beverages():
    def __init__(self, name, price,input):
        self.name   = name
        self.price  = float(price)
        self.input = input
    def toString(self):
        bev_det =(bcolors.red+"### {0} ###\n"
                       .format(self.name)+
                       "Price  :"+bcolors.green+"${0}\n"
                       .format(self.price)+bcolors.red+
                       "Input  :"+(bcolors.blue+"[{0}]"
                       .format(self.input))+bcolors.black)
        print(bev_det)