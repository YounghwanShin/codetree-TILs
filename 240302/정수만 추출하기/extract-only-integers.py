A,B=input().split()

def check_int(arr):
    string=''
    for char in arr:
        if char.isdigit():
            string+=char
        else:
            break
    return int(string)

print(check_int(A)+check_int(B))