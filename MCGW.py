def Solver():
    S = genStates()
    G = genGraph(S)
    s = "EEEE" #source node
    d = "WWWW" #destination node
    result = genShortestPath(G,s,d)
    for i in range(1,len(result)): #print the path in text
        if result[i][0] == "E":
            direction = "east"
        else:
            direction = "west"
        posit = 0
        for j in range(1,4):
            if result[i-1][j] != result[i][j]:
                posit = j
        if posit == 1:
            who = "the cabbage"
        elif posit == 2:
            who = "the goat"
        elif posit == 3:
            who = "the wolf"
        else:
            who = "himself"
        print(str(i) + ". " + "The man takes " + who + " to the " + direction + ".")

    
def genStates(): #generates all 16 states
    side = ("E", "W")
    states = []
    for i in side:
        for j in side:
            for k in side:
                for l in side:
                    aState = i + j + k + l
                    states.append(aState)
    return states

def genGraph(S):
    G = []
    graph={} #create dictionary for the Graph
    for i in range(len(S)):
        if isLegal(S[i]) == True:
            G.append(S[i])
            
    for i in range(len(G)):
        result1 = nextStates(G[i],G)
        graph.update({G[i]:result1[1:]}) #add possible states to each legal states, put it in graph
    return graph
            
def isLegal(S): #called by genGraph(S), check if the states are legal.
                #used if-statement to check if the states meet the constraints.
    if (S[1] == S[2] and S[0] != S[1] and S[0] != S[2]) or (S[2] == S[3] and S[0] != S[3] and S[0] != S[2]):
        return False
    else:
        return True
    #return True or False Boolean value
    
def nextStates(startnode,allstates):
    possible=[startnode]        
    c1 = startnode.count("E") #count no. of E and W
    c2 = startnode.count("W")
    for i in range(len(allstates)): #check the change of E to W and W to E.
        if allstates[i].count("E") - c1 <= 2 and allstates[i].count("E") - c1 >= -2 and allstates[i].count("W") - c2 <=2 and allstates[i].count("W") - c2 >=-2 and startnode[0] != allstates[i][0]:
            c = 0
            for j in range(4):
                if allstates[i][j] == startnode[j]:
                    c += 1
            if c >= 2:
                possible.append(allstates[i])
    return possible

def genShortestPath(graph, start, end, path=[]): #find the shortest path. recursion method
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = genShortestPath(graph, node, end, path)
            shortest = newpath
    return shortest

Solver()

