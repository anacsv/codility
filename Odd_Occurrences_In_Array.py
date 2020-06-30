def solution(A):
    
    for item in A:
        if A.count(item) %2 == 1:
            return item   

print(solution([9,1,2,9,1]))       
