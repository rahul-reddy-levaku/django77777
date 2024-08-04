def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

def count_digits(num):
    c=0
    while c>0:
        c+=1
        num=num//10
    return c