n=int(input())

num=0

def calculate(grade_arr):
    grade_standard=[(60,'pass'),(0,'fail')]

    global num

    for grade,message in grade_standard:
        if sum(grade_arr)/len(grade_arr)>=grade:
            if message=='pass':
                num+=1
            return message

for _ in range(n):
    grade_arr=list(map(int, input().split()))
    print(calculate(grade_arr))

print(num)