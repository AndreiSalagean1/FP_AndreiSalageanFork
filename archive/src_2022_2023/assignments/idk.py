def create_q(num: int ,den: int) ->dict:
    """

    :param num:
    :param den:
    :return:
    """
    return {"num": num , "den": den}

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