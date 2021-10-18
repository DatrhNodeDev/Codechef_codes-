# cook your dish here
n=int(input())
for i in range (n):
    (a,b,c) = map(int, input().split())
    f=1
    if(a==0):
        if(b==1 or c==1):
            f=0
        elif((b==0 and c==1 ) or (b==1 and c==0)):
            f=0
    else:
        if(b==0 or c==0):
            f=0
        elif((b==0 and c==1 ) or (b==1 and c==0)):
            f=0
    if(f==1):
        print(0)
    else:
        print(1)