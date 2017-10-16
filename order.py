import menu
from colour import bcolors

def res():
    def again():
        while True:
            ans = input("Order another Burger [Y/N]?").upper()
            if ans == "Y":minterface()
            else:check()

    def check():
        print(bcolors.blue +
              "###################\n"
              "#_____CHECKOUT____#\n"
              "###################\n" + bcolors.black +
              "Order List  :{0}\nTotal Price :".format(menu.food_list) + bcolors.green +
              "${0}\n".format(sum(menu.cost)) + bcolors.black)

    def minterface():
        rui = input(bcolors.blue+
                    "##########################\n"
                    "#______DON'S BURGER!_____#\n"
                    "##########################\n"+bcolors.black+
                    "[1] Burgers\n"+"[2] Side Courses\n"+
                    "[3] Beverages\n"+"[4] Checkout\n"+
                    bcolors.red+"[Q] Leave\n"+bcolors.black+
                    "Enter Selection :").upper()
        if   rui == "1":binterface()
        elif rui == "2":sinterface()
        elif rui == "3":dinterface()
        elif rui == "4":check()
        elif rui == "Q":quit()
        else:menu.falseinput(),minterface()

    def binterface():
        bui = input(bcolors.blue+
                    "########################\n"
                    "#________BURGERS_______#\n"
                    "########################\n"+
                    bcolors.black+"[1] Plain Burger\n[2] Cheese Burger\n"+
                    "[3] Original Burger\n[4] Double Cheese Burger\n[Q] Back\n"+
                    bcolors.black+"Enter Selection :").upper()
        if   bui == "1":menu.burg (),again()
        elif bui == "2":menu.cburg(),again()
        elif bui == "3":menu.oburg(),again()
        elif bui == "4":menu.dburg(),again()
        elif bui == "Q":minterface()
        else:menu.falseinput(), binterface()

    def sinterface():menu.scourse(),again()
    def dinterface():menu.bvrage(),again()
    minterface()