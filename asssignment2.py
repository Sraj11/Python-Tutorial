def fact(n):
    '''ITERATIVE FUNCTION OF THE FACTORIAL'''
    f=1
    for i in range(1,n+1):
        f=f*i
        print(f)
    print("final",f)

fact(5)


def fact1(n):
    '''Recursive function of factorial of number'''
    if n==1:
        return 1
    else:
        return  n*fact1(n-1)
print(fact1(3))

def compute(x,n):
    '''computing x^n/n!'''
    return x**n/fact1(n)

# print(compute(2,5))

def sum1(x,n):
    '''summation of f(x,n)=1+summationof(x^n/n!)'''
    s=0
    for i in range(1,n+1):
        s=s+x**i/fact1(i)
    return s+1
print(sum1(4,5))


def sum5(x,n):
    '''calculating function and comparing with some null value'''
    small_number=float(input('enter number'))
    if sum1(x,n)-sum1(x,n-1)<small_number:
        print('ok')


sum5(3,5)



def sum6(p,q):
    '''computing the function v1=f(p,100)*f(q,100) and f(p+q,100) and calculating the difference'''
    v1=sum1(p,100)*sum1(q,100)
    v2=sum1(p+q,100)
    difference=v1-v2
    print(difference)

