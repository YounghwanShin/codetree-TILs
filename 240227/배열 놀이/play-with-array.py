n,q=map(int,input().split())

arr=list(map(int, input().split()))

for _ in range(q):
    arr_question=list(map(int, input().split()))
    if arr_question[0]==1:
        a=arr_question[1]
        print(arr[a-1])
    elif arr_question[0]==2:
        a=arr_question[1]
        if a in arr:
            print(arr.index(a)+1)
        else:
            print(0)
    else:
        a,b=arr_question[1],arr_question[2]
        for i in range(a-1,b):
            print(arr[i],end=' ')
    arr_question=[]