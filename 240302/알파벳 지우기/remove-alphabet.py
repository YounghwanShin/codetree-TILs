A=input()
B=input()

def check_int(arr):
    string=''
    for char in arr:
        if char.isdigit():
            string+=char
        else:
            continue
    return int(string)

print(check_int(A)+check_int(B))