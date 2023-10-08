#5. Generate the largest prime number smaller than a given natural number `n`. If such a number does not exist, a message should be displayed.


def prime(x):
    ok=True
    for i in range(2,x//2):
        if x % i == 0:
            ok=False

    if ok==True:
        return 1
    else:
        return 0


def main():
    n=int(input("Input n: "))
    for i in range(n-1,2,-1):
        if prime(i)==1:
            print("largest prime number smaller than ",n," is ",i)
            return

    print("no such number")


main()