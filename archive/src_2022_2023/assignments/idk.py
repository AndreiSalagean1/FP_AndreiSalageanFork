from random import randint
from math import gcd

def create_q(num: int ,den: int) ->dict:
    """

    :param num:
    :param den:
    :return:
    """
    g=gcd(num,den)
    return {"num": num//g , "den": den//g}

def to_str(q:dict)->str:
    """

    :param q:
    :return:
    """
    return str(q["num"]) + "/" + str(q["den"])

print(create_q(1,4))
print(to_str(create_q(1,4)))

data = [create_q(1,2),create_q(2,3),create_q(4,5)]
print(data)

for i in range(0,len(data)):
    print(to_str(data[i]))

for q in data:
    print(to_str(q))

while True:
    print("1.add a number")
    print("2.Display numbers")
    print("3.Add a Generated random number")
    print("0.exit")


    option=input(">")

    if option=="1":
        number_str=input("Input number ")
        token=number_str.split("/")
        numerator=int(token[0])
        denominator=int(token[1])
        data.append(create_q(numerator,denominator))
        pass
    elif option=="2":
        print("The list is : ")
        for q in data:
            print(to_str(q),end=', ')

        print("\n")
        pass
    elif option=="3":
        numerator=randint(-10,10)
        denominator=randint(1,10)
        data.append(create_q(numerator,denominator))

    elif option=="0":
        print("bye")
        break
