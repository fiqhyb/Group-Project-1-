import time
from inheritance import *

food_list = []
cost = []
def burg():
    bburg = Burger("Plain Chicken Burger", "Chicken", 3.45,1)
    cburg = Burger("Plain Beef Burger", "Beef", 3.75,2)
    fburg = Burger("Plain Fish Burger", "Fish", 3.75,3)
    pburg = Burger("Plain Ham Burger", "Pork", 4.05,4)
    print(bcolors.yellow +
          "########################\n"
          "#_____Plain Burger_____#\n"
          "########################" + bcolors.black)
    bburg.toString(),cburg.toString(),fburg.toString(),pburg.toString()
    choice = input("[Q] Back\nEnter Selection :").upper()
    if   choice == "1":food_list.append(bburg.name),cost.append(bburg.price)
    elif choice == "2":food_list.append(cburg.name),cost.append(cburg.price)
    elif choice == "3":food_list.append(fburg.name),cost.append(fburg.price)
    elif choice == "4":food_list.append(pburg.name),cost.append(pburg.price)
    elif choice == "Q":return
    else: falseinput(),burg()
    print(bcolors.green+"Choice has been added to checkout"+bcolors.black),time.sleep(3)

def cburg():
    cbburg = Cheeseburger("Chicken Cheese Burger", "Chicken", "Cheese", 3.85,1)
    ccburg = Cheeseburger("Beef Cheese Burger", "Beef", "Cheese", 4.15,2)
    cfburg = Cheeseburger("Fish Cheese Burger", "Fish", "Cheese", 4.15,3)
    cpburg = Cheeseburger("Ham Cheese Burger", "Pork", "Cheese", 4.45,4)
    print(bcolors.yellow +
          "#######################\n"
          "#____Cheese Burger____#\n"
          "#######################" + bcolors.black)
    cbburg.toString(),ccburg.toString(),cfburg.toString(),cpburg.toString()
    choice = input("[Q] Back\nEnter Selection :").upper()
    if   choice == "1":food_list.append(cbburg.name),cost.append(cbburg.price)
    elif choice == "2":food_list.append(ccburg.name),cost.append(ccburg.price)
    elif choice == "3":food_list.append(cfburg.name),cost.append(cfburg.price)
    elif choice == "4":food_list.append(cpburg.name),cost.append(cpburg.price)
    elif choice == "Q":return
    else: falseinput(),cburg()
    print(bcolors.green+"Choice has been added to checkout"+bcolors.black),time.sleep(3)

def oburg():
    obburg = Compburger("Chicken Burger", "Chicken", "Cheese", "Lettuce", 5.65,1)
    ocburg = Compburger("Beef Burger", "Beef", "Cheese", "Lettuce", 5.95,2)
    ofburg = Compburger("Fish Burger", "Fish", "Cheese", "Lettuce", 5.95,3)
    opburg = Compburger("Ham Burger", "Pork", "Cheese", "Lettuce", 6.25,4)
    print(bcolors.yellow +
          "#######################\n"
          "#___Original Burger___#\n"
          "#######################" + bcolors.black)
    obburg.toString(), ocburg.toString(), ofburg.toString(), opburg.toString()
    choice = input("[Q] Back\nEnter Selection :").upper()
    if   choice == "1":food_list.append(obburg.name),cost.append(obburg.price)
    elif choice == "2":food_list.append(ocburg.name),cost.append(ocburg.price)
    elif choice == "3":food_list.append(ofburg.name),cost.append(ofburg.price)
    elif choice == "4":food_list.append(opburg.name),cost.append(opburg.price)
    elif choice == "Q":return
    else: falseinput(),oburg()
    print(bcolors.green+"Choice has been added to checkout"+bcolors.black),time.sleep(3)

def dburg():
    dbburg = Doubcheburg("Double Cheese Chicken Burger", "Chicken", "Cheese", "Beef", "Cheese", 6.20,1)
    dcburg = Doubcheburg("Double Cheese Beef Burger", "Beef", "Cheese", "Beef", "Cheese", 6.50,2)
    dfburg = Doubcheburg("Double Cheese Fish Burger", "Fish", "Cheese", "Fish", "Cheese", 6.50,3)
    dpburg = Doubcheburg("Double Cheese Ham Burger", "Pork", "Cheese", "Pork", "Cheese", 6.80,4)
    print(bcolors.yellow+
          "########################\n"
          "#_Double Cheese Burger_#\n"
          "########################"+bcolors.black)
    dbburg.toString(),dcburg.toString(),dfburg.toString(),dpburg.toString()
    choice = input("[Q] Back\nEnter Selection :").upper()
    if   choice == "1":food_list.append(dbburg.name),cost.append(dbburg.price)
    elif choice == "2":food_list.append(dcburg.name),cost.append(dcburg.price)
    elif choice == "3":food_list.append(dfburg.name),cost.append(dfburg.price)
    elif choice == "4":food_list.append(dpburg.name),cost.append(dpburg.price)
    elif choice == "Q":return
    else: falseinput(),dburg()
    print(bcolors.green+"Choice has been added to checkout"+bcolors.black),time.sleep(3)

def scourse():
    sofres = Sidecourse("Onion Fries", 2.30,1)
    sffres = Sidecourse("French Fries", 2.50,2)
    ssalad = Sidecourse("Caesar Salad", 2.50,3)
    print(bcolors.green+
          "#######################\n"
          "#_____Side Course_____#\n"
          "#######################" + bcolors.black)
    sofres.toString(), sffres.toString(), ssalad.toString()
    choice = input("[Q] Back\nEnter Selection :").upper()
    if   choice == "1":food_list.append(sofres.name),cost.append(sofres.price)
    elif choice == "2":food_list.append(sffres.name),cost.append(sffres.price)
    elif choice == "3":food_list.append(ssalad.name),cost.append(ssalad.price)
    elif choice == "Q":return
    else: falseinput(),scourse()
    print(bcolors.green+"Choice has been added to checkout"+bcolors.black),time.sleep(3)

def bvrage():
    soda  = Beverages("Soda", 2.10,1)
    milk  = Beverages("Milk", 1.90,2)
    tea   = Beverages("Tea", 1.60,3)
    print(bcolors.pink+
          "#####################\n"
          "#_____Beverages_____#\n"
          "#####################" + bcolors.black)
    soda.toString(), milk.toString(), tea.toString()
    choice = input("[Q] Back\nEnter Selection :").upper()
    if   choice == "1":food_list.append(soda.name),cost.append(soda.price)
    elif choice == "2":food_list.append(milk.name),cost.append(milk.price)
    elif choice == "3":food_list.append(tea.name),cost.append(tea.price)
    elif choice == "Q":return
    else: falseinput(),bvrage()
    print(bcolors.green+"Choice has been added to checkout"+bcolors.black),time.sleep(3)

def falseinput():
    print(bcolors.red+
          "Input unidentified\n"
          "Please enter known input!"+
          bcolors.black)