def solution(A,K):
    i = 0

    if len(A) != 0:
        while i < K:
            B = A[-1:] 
            C = B + A
            C.pop()
            A = C
            i += 1
    return A 

print(solution([1,3],0))