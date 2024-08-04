x=100
def fun1():
    print("inside fun1 at package level")
def is_odd(num):
    return num%2!=0
def is_even(num):
    return num%2==0

def is_prime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    return c==2
