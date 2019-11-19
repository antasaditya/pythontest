"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def traverseAndCopy(self, node, nodeMap):
        nodeMap[node] = Node(node.val, []);
        for nbr in node.neighbors:
            if(nbr not in nodeMap): 
                self.traverseAndCopy(nbr, nodeMap)
            
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeMap = {}
        self.traverseAndCopy(node, nodeMap)
        
        for orig,copy in nodeMap.items():
            copy.neighbors = [nodeMap[x] for x in orig.neighbors]
            
        return nodeMap[node]