#7. Determine the twin prime numbers `p1` and `p2` immediately larger than the given non-null natural number `n`. Two prime numbers `p` and `q` are called twin
# if `q - p = 2`.


def prime(x):
    ok=True
    for i in range(2,x//2):
        if x % i == 0:
            ok=False

    if ok==True:
        return 1
    else:
        return 0



def next_prime(x):
    i=int(x)
    while(True):
        i+=1
        if prime(i)==1:
            return i
def main():

    n=int(input("Input n: "))

    while True:
        n=int(next_prime(n))
        p2=int(next_prime(n))
        if(p2-n==2):
            print(n,"  ",p2)
            return







main()