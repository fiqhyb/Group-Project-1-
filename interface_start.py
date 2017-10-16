import order as a
import office as b

balance = [0]
def inter():
    choice = input("########################\n"
                   "Where do you want to go?\n"
                   "[1] Office\n[2] Restaurant\n"
                   "[3] Balance\n"
                   "[Q] Quit\nEnter Selection :").upper()
    if   choice == "1":b.Office()
    elif choice == "2":a.res()
    elif choice == "3":
        print("############\nYour balance :${0}".format(sum(balance)))
        inter()
    elif choice == "Q":quit()
inter()