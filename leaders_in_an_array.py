def leaders_in_an_array(A):
    leaders=[]
    max_right=float('-inf')
    for i in range(len(A)-1, -1, -1):
        if A[i]>max_right:
            leaders.append(A[i])
            max_right = A[i]
    leaders.reverse()
    return leaders
A = list(map(int,input().split()))
print(leaders_in_an_array(A))
