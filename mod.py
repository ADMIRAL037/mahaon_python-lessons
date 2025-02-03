class kl():
    pass
def dekorate():
    def wrapper(v0,v,t):
        a=A(v0,v,t)
        s=(v0*t) + ((a*t**2)/2)
    return wrapper
def A(v0,v,t):
    a=(v-v0)/t
    return a
try:
    v0=int(input())
    v=int(input())
    t=int(input())

    if t==0:
        raise MyException('больше 0')
    print (A(v0,v,t))


except ValueError:
    print('является строкой')




