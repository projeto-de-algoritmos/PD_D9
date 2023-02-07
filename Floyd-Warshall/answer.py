n = int(input())
matrix = [[] for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))
    
deleted = list(map(lambda x: int(x) - 1, input().split()))
 
 
s = 0
a = []
sums = []
 
for i in range(n):
    u = deleted.pop(-1)
    matrix[u][u] = 0
    for j in range(i):
        m = matrix[u][a[j]]
        
        for k in range(i):
            m = min(m, matrix[u][a[k]] + matrix[a[k]][a[j]])
        
        matrix[u][a[j]] = m
        s += m
        m = matrix[a[j]][u]
        
        for k in range(i):
            m = min(m, matrix[a[j]][a[k]] + matrix[a[k]][u])
        
        matrix[a[j]][u] = m
        s += m
    
    for j in range(i):
        for k in range(i):
            if j != k:
                aux = matrix[a[j]][u] + matrix[u][a[k]]
                if matrix[a[j]][a[k]] > aux:
                    s += aux - matrix[a[j]][a[k]]
                    matrix[a[j]][a[k]] = aux
    
    sums.append(s)
    
    a.append(u)

sums.reverse()

print(" ".join(map(str, sums)))