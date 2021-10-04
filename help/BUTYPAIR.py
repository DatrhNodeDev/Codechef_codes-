try:
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        c,i=0,0
        while i<n:
            j=0
            while j<n:
                if i!=j and(((a[i]-a[j])/a[i])<((a[i]-a[j])/a[j])):
                    c+=1
                j+=1
            i+=1
        print(c)
except:
    pass
