
def solution(N):
    result = 0
    i = 1
    n_bin = bin(N)[2:]

    while i <= len(n_bin) - 2:
        if '1' + i * '0' + '1' in n_bin:
            result = i 
        i += 1 
    print('N='+n_bin)    
    return result 
         
print('resultado:'+ str(solution(32)))
print('resultado:'+ str(solution(9)))

