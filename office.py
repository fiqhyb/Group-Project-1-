import random
import work
from colour import bcolors
import interface as i

def Office():
    print(bcolors.blue+"####THE OFFICE####"+bcolors.black)
    office = int(input("[1] Normal"
                       "\n[2] Work Hard"
                       "\n[3] Take It Easy\n"
                       "Enter Selection :"))
    wage = random.randint(150,200)
    if office == 1:
        work1 = wage
        work.normal()
        i.balance.append(work1)
        print("Your wage today:${0}".format(work1))

    elif office == 2:
        work2 = wage+(wage*(75/100))
        work.hard()
        i.balance.append(work2)
        print("Your wage today:${0}".format(work2))
    elif office == 3:
        work3 = wage-(wage*(50/100))
        work.easy()
        i.balance.append(work3)
        print("Your wage today:${0}".format(work3))
    i.inter()