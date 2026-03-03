from itertools import count


def eight(n):
    n=int(input())
    s=[]#生成一个空栈
    if n==0:
        print(n)
    else:
        a=n%8
        s.append(a)
        n=n//8
        while len(s)!=0:
            e=s[0]
            print(e)
eight(95)
