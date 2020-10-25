
def f (a, b):
    if a==b:
        print('gsd is', a)
        return
    elif a>b:
        n=a-b
        f (n,b)
    elif a<b:
        n=b-a
        f (a,n)

a =7 #int(input())
b =3 #int(input())
f(a,b) +1

