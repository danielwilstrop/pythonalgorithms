#Dijkstra's Algorithm
#For finding the best 'route' in a weighted graph

#Basic graph for example and testing 
graph = {}

#'Start' node is a hash table, keys are the neibouring nodes, values are the weights
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

#Same principle for nodes 'a' and 'b'
graph['a'] = {}
graph['a']['finish'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['finish'] = 5

#The 'finish" node wont have any neighbours
graph['finish'] = {}

#Costs hash table - cost (value) to get to the node (key) from the start
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['finish'] = infinity

#Final hash table for the parents of each node 
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

#Array to keep track of which nodes have been inspected 
processed = []

#Finds the lowest cost node - util function for the main algorithm
def lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#Main Dijkstra's Algorithm
def dijk(graph, costs, parents):
    node = lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = lowest_cost_node(costs)
        return costs['finish']  #returns the value of the cheapest combined route 


#Tests
print(dijk(graph, costs, parents))




