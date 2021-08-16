#Breadth Frist Search - Basic Graph Search algorithm

from collections import deque

def breadth_first_search(name, graph):
    search_queue = deque()  #creates a queue
    search_queue += graph[name]
    searched = []  #keep track of which nodes have been searched 

    while search_queue:
        node = search_queue.popleft()
        if not node in searched:
            if node == name:
                print(name + "found")
                return True
            else:
                search_queue += graph[node]
                searched.append(node)
    return False

#Test
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

print(breadth_first_search('alice', graph))

