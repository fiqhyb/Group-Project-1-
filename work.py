import random

def easy():
    def loop():
        while True:
            equation = input("Answer :")
            if int(equation) == a+b:
                break
            else: print("false")
    for i in range (1):
        a = random.randint(1,10)
        b = random.randint(1,10)
        print("Solve this equation!\n"
              "{0} + {1} =".format(a,b))
        loop()
def normal():
    def loop():
        while True:
            equation = input("Answer :")
            if int(equation) == a+b:
                break
            else: print("false")
    for i in range (2):
        a = random.randint(1,10)
        b = random.randint(1,10)
        print("Solve this equation!\n"
              "{0} + {1} =".format(a,b))
        loop()
def hard():
    def loop():
        while True:
            equation = input("Answer :")
            if int(equation) == a+b:
                break
            else: print("false")
    for i in range (3):
        a = random.randint(1,10)
        b = random.randint(1,10)
        print("Solve this equation!\n"
              "{0} + {1} =".format(a,b))
        loop()