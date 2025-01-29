    ## COMP 550 Algorithms

# BFS
def BFS(G, s):
    s -= 1
    d = [-1] * len(G)
    d[s] = 0
    Q = []
    Q.append(s)
    while len(Q) > 0:
        u = Q.pop(0)
        for v in G[u]:
            if (d[v - 1] == -1):
                d[v - 1] = d[u] + 1
                Q.append(v - 1)
    
    return d

# DFS
def DFS(G):
    pre = ['inf'] * len(G)
    post = ['inf'] * len(G)
    t = 1
    
    # for(u in range(len(G))):
    #     if(pre[u] == 'inf'):
    #         pre, post, t = Explore(G, u, pre, post, t)

    return pre, post
        

# DFS Helper -> Explore
def Explore(G, u, pre, post, t):
    pre[u] = t
    t += 1
    for v in G[u]:
        if pre[v - 1] == 'inf':
            pre, post, t = Explore(G, v - 1, pre, post, t)
        
    post[u] = t
    t += 1
    return pre, post, t

# DFS Helper -> Back Edge Finder
def BackEdges(G, pre, post):
    m = []
    for v in range(len(G)):
        for u in G[v]:
            if (pre[u - 1] < pre[v] < post[v] < post[u - 1]):
                m.append([v + 1, u])
    
    return m


# G = []
# pre, post = DFS(G)
# m = BackEdges(G, pre, post)
# print(m)
    
    
# Prim's Algorithm
def Prim(G):
    # Set S should be a binary array of length n
    S = [0] * len(G)
    S[0] = 1
    F = []
    count = 1
    
    while count < len(G):
        e = 'inf'
        v = 'inf'
        w = 'inf'
        
        # Find lightest edge crossing S
        for i in range(0, len(S)):
            if(S[i] == 1):
                # For edges in G of this index find edge weights
                # m = [v, w]
                for m in G[i]:
                    # If v is not in S (edge is crossing s) AND weight is < current min
                    v_m = m[0]
                    w_m = m[1]
                    if(S[v_m - 1] == 0 and (w == 'inf' or w > w_m)):
                        w = w_m
                        v = v_m
                        e = [i + 1, v]
        
        # Add v to S; add e to F
        S[v - 1] = 1
        F.append(e)
        count += 1
    
    return F

# Running Prim's Algorithm
# G = []
# F = Prim(G)
# print(F)
    
    
# Selecting Compatible Intervals
def SCI(A):
    # Sort A by non-decreasing end time
    B = []
    while len(A) > 0:
        index = 0
        min = A[index][1]
        for i in range(len(A)):
            if A[i][1] < min:
                index = i
                min = A[index][1]
        B.append(A.pop(index))
    
    # Adding S
    S = []
    S.append(B[0])
    for i in range(1, len(B)):  
        # If e does not conflict with the last interval in S (e_p), add e
        e = B[i]
        e_p = S[len(S) - 1]
        if(e_p[1] < e[0]):
            S.append(e)
            
    return S
    
# Running Selecting Compatible Intervals
# A = []
# S = SCI(A)
# print(S)


# Fractional Knapsack -> outputs X and the optimal value 'opt'
def FKnap(v, w, B):
    wc = []
    vc = []
    
    # sort items by non-increasing v[i]/w[i]
    while len(v) > 0:
        index = 0
        m = v[index] / w[index]
        for i in range(len(v)):
            mi = v[i] / w[i]
            if (mi > m):
                index = i
                m = mi
        vc.append(v.pop(index))
        wc.append(w.pop(index))
    
    # creating X
    X = [0.00] * len(vc)
    curr_b = 0.00
    opt = 0.00
    for i in range(len(vc)):
        # whichever is smaller between: (the remainder of weight we have to add / the current weight of i) AND (1)
        X[i] = min(((B - curr_b) / wc[i]), 1.00)
        curr_b += X[i] * wc[i]
        opt += vc[i] * X[i]
        
    return X, opt
    

# Running Fractional Knapsack
# v = []
# w = []
# B = x
# X, opt = FKnap(v, w, B)
# print(X)