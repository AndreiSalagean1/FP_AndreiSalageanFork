#15. Generate the largest perfect number smaller than a given natural number `n`. If such a number does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its divisors,
# except itself. (e.g.  `6 is a perfect number, as 6=1+2+3`).

def sum_div(x):
    sum=0
    for i in range (1,x-1):
        if x%i==0:
            sum=sum+i

    return sum

def perfect_number(x):
    if sum_div(x)==x :
        return 1
    return 0


def main():
    n=int(input ("input n "))
    for i in range(n-1,1,-1):
        if(perfect_number(i)==1):
            print (i)
            return
    print("no such number")


main()

""""


"""