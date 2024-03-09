n_1, n_2 = map(int, input().split())
A = input().split()
B = input().split()

def arr(a, b, A, B):
    b_str = ' '.join(B)
    for i in range(a - b + 1):
        a_sub_str = ' '.join(A[i:i+b])
        if a_sub_str == b_str:
            return True
    return False

if arr(n_1, n_2, A, B):
    print('Yes')
else:
    print('No')