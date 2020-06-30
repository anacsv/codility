#Find value that occurs in odd number of elements, Lesson 2B codility (Odd Ocurrences in Array)

def solution(A):    
    # se o tamanho da lista for igual a 1 retorna o unico item da lista
    if len(A) == 1:
         return A[0]
    #ordena a lista em ordem crescente     
    A.sort()
    #itera a lista de 0 até o tamanho da lista A, de 2 em 2 
    for i in range(0 , len (A) , 2):
        #retorna o ultimo da item da lista se este for o se par
        if i+1 == len(A):
            return A[i]
        #se o item da posiçao i for diferente do item da posiçao i + 1 retorna o item A[i]    
        if A[i] != A[i+1]:
            return A[i]
#List for test
print(solution([9,3,9,3,9,7,9])) 