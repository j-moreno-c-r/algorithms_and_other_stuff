import json

#paths
graph= {}
graph["you"]=["alice","bob","claire"]
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5
#costs
infinite = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinite
#parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None
#marked as processed
processed = []
def find_lower_cost(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos: 
        custo = custos[nodo]
        if custo<custo_mais_baixo and nodo not in processed: 
            custo_mais_baixo = custo 
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = find_lower_cost(costs)
while nodo is not None:
    costs = costs[nodo]
    nodo = (costs) 
while nodo is not None: 
    costs = costs[nodo]
    vizinhos = graph[nodo]
    for n in vizinhos.keys(): 
        new_cost = costs + vizinhos[n]
        if costs[n] > new_cost: 
            costs[n] = new_cost 
            parents[n] = nodo 
    processed.append(nodo)
    nodo = find_lower_cost(costs) 