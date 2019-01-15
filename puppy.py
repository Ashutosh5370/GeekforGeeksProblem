#Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 otherwise decrement its value by


N = int(input())


def fun(n):
    if n%4==0:
        return  n+1
    else:
        return n-1

print(fun(N))