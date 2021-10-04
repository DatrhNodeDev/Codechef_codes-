for _ in range(int(input())):
    n,k = map(int,input().split())
    if n-k != 1:
        ans = []
        for i in range(1,k+1):
            ans.append(str(i))
        for i in range(k+1,n+1):
            if i != n:
                ans.append(str(i+1))
            else:
                ans.append(str(k+1))
        print(" ".join(ans))
    else: print(-1)