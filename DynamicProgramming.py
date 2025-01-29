        # Comp 550 Dynamic Programming Algorithms

# Max in array
def arr_max(A):
    m_i = 0
    m = A[0]
    for i in range(1, len(A)):
        if(m < A[i]):
            m = A[i]
            m_i = i
    return m, m_i

# Longest Increasing Sub-sequence
def LIS(A):
    d = [1] * len(A)
    for i in range(1, len(A)):
        # Find RHS of recurrence
        max_dj = 0
        for j in range (0, i):
            if(A[j] < A[i]):
                max_dj = max(max_dj, d[j])
        d[i] += max_dj
    return arr_max(d), d

# Find max subsequence of LIS given d
def MSub(A, d: list):
    m, m_i = arr_max(d)
    L = []
    L.append(A[m_i])
    
    while(len(L) < m):
        for j in range(0, m_i):
            if(d[j] == d[m_i] - 1 and A[j] < L[len(L) - 1]):
                L.append(A[j])
                m_i = j
                break
    return L
        
# Running LIS
# A = []
# max, d = LIS(A)
# for i in range(0, len(A)):
#     print(d[i], A[i], "\n")
# print(MSub(A, d))

# 0/1 Knapsack
def fKnapsack(v, w, B):
    # d[r][c]
    d = [0]*len(v)
    for i in range(0, len(v)):
        d[i] = [0] * (B + 1)
    
    for j in range(0, B + 1):
        if j < w[0]:
            d[0][j] = 0
        else :
            d[0][j] = v[0]
    
    for i in range(1, len(v)):
        for j in range(1, B + 1):
            if(j < w[i]):
                d[i][j] = d[i - 1][j]
            else:
                d[i][j] = max(d[i - 1][j], v[i] + d[i - 1][j - w[i]])
    
    return d[len(v) - 1][B]

# Running 0/1 Knapsack
# v = []
# w = []
# B = x
# print(fKnapsack(v, w, B))

# Stack block
def stack_block(R, B, n):
    # Indexing d starting at 0
    d = (n + 1) * [1]
    L = max(R, B)
    S = min(R, B)
    C = 0

    # Base case
    if(L % S == 0):
        C = L
    else:
        C = L + S
    d[C] = 2
    
   # Induction
    for i in range(C + 1, n + 1):
        # If this is true it means the value is reachable given R, B
        if(d[i - R] > 1 or d[i - B] > 1 or (i % R == 0 and i % B == 0)):
            d[i] = d[i - R] + d[i - B]
        else:
            d[i] = 1

    return d[n]


# Bellman-Ford
def bFord(G, s):
    # Setting all vertex values in G to v - 1
    for v in range(0, len(G)):
        for u in range(0, len(G[v])):
            G[v][u][0] -= 1
    s -= 1
    
    # d[v][j]
    d = [0]*len(G)
    for i in range(0, len(G)):
        d[i] = ['inf'] * (len(G) + 1)
        
    for j in range(0, len(G) + 1):
        d[s][j] = 0
    
    for j in range(1, len(G) + 1):
        for v in range(0, len(G)):
            # If v == s we want the entire row to be 0 (since we are starting there)
            if(v != s):
                # We must check all outneighbors of v
                min_weight = 'inf'
                minl = 'inf'
                inn = -1
                # Finding the minimum weighted in-neighbor of v
                for m in range(0, len(G)):
                    if(d[m][j - 1] != 'inf'):
                        for u in range(0, len(G[m])):
                            # If this is true then m == in neighbor of v
                            if(G[m][u][0] == v):
                                if(min_weight == 'inf' or G[m][u][1] + d[m][j - 1] < min_weight):
                                    minl = G[m][u]
                                    inn = m
                                    min_weight = minl[1] + d[m][j - 1]
                                
                a = d[v][j - 1]
                b = d[inn][j - 1]
                c = minl[1]
                
                if(min_weight == 'inf'):
                    d[v][j] = a
                elif(a == 'inf'):
                    d[v][j] = min_weight
                else:
                    d[v][j] = min(a, min_weight)
    
    # Concatinating d into what we want
    r = []
    for v in range(len(G)):
        r.append(d[v][len(G)])
    return r

# Running bellman-ford
# G = []
# # s = 1
# print(bFord(G, s))


# Djikstra's algorithm
def dijkstra(G, s):
    # Setting all vertex values in G to v - 1
    for v in range(0, len(G)):
        for u in range(0, len(G[v])):
            G[v][u][0] -= 1
    s -= 1
    
    # base cases / initializing
    d = [float('inf')] * len(G)
    d[s] = 0
    S = [0] * len(G)
    S[s] = 1
    count = 1
    
    while (count < len(G)):
        # Find lightest edge crossing S
        v = 'inf'
        w = 'inf'
        parent = -1
        for i in range(0, len(S)):
            if(S[i] == 1):
                # For edges in G of this index find edge weights
                # m = [v, w]
                for m in G[i]:
                    # If v is not in S (edge is crossing s) AND weight is < current min
                    if(S[m[0]] == 0 and (w == 'inf' or w > m[1])):
                        w = m[1]
                        v = m[0]
                        parent = i
                        
        # add v to S
        if(parent != -1):
            S[v] = 1
            d[v] = min(d[v], w + d[parent])
            count += 1
        
    return d
                        
# Running Dijsktra's
# G = []
# s = 1
# print(dijkstra(G, s))
