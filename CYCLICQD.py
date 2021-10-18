T=int(input())
for i in range(T):
    (a,b,c,d)=map(int,input().split(" "))
    if(a+c==b+d==180 ):
        print("YES")
    else:
        print("NO")
        
