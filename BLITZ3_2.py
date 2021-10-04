try:
    n=int(input())
    
    for i in range(0,n):
        arr=list(map(int,input().split()))

        turns=arr[0]

        time=2*(180+turns)
        time_left=arr[1]+arr[2]
        dur=time-time_left
        print(dur)
except EOFError as e:pass
