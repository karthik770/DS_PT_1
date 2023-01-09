
INF = 9999999
V = 6 
G = [[0, 4, 4, 0, 0, 0],
     [4, 0, 2, 0, 0, 0],
     [4, 2, 0, 3, 2, 4],
     [0, 0, 3, 0, 0 , 3],
     [0, 0, 2, 0, 0, 3],
     [0, 0 ,4 ,3, 3, 0]
     ]
     
selected = [0, 0, 0, 0, 0,0]
no_edge = 0
selected[0] = True
print("Edge : Weight\n")
while (no_edge < V - 1): # 0, 5
    minimum = INF # 9999999
    x = 0
    y = 0
    for i in range(V): #6 rows
        if selected[i]: #A/ 0
            for j in range(V):  # column
                if ((not selected[j]) and G[i][j]):  #G[AB] - 4
                    if minimum > G[i][j]: #9999999>4
                        minimum = G[i][j] # min= 4
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1