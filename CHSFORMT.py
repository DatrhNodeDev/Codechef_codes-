# cook your dish here
try:
    n=int(input())

    for i in range(0,n):
        ar=list(map(int,input().split()))
        a=ar[0]
        b=ar[1]
        x=a+b
        if(x<3):
            print('1')
        elif(x>=3 and x<=10):
            print('2')
        elif(x>=11 and x<=60):
            print('3')
        elif(x>60):
            print('4')

except EOFError as e:pass

