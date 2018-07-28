T=int(input())
arr=[0]
temp1=[]
temp2=[]
for x in range(T):
    N,K=input().split()
    arr=input().split()
    arr = list(map(int,arr))
    rem=int(K)%int(N)
    for y in range(int(N)):
        if((rem-y)==0):
            temp1=arr[0:y]
            temp2=arr[y:int(N)]
            arr=(temp2+temp1).copy()
            break
for x in arr:
    print(x,end=" ")
