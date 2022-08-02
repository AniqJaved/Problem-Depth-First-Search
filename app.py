class Node:
    def __init__(self,name):
        self.childern = []
        self.name = name
    def addChild(self,name):
        self.childern.append(Node(name))
    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.childern:
            child.depthFirstSearch(array)
        return array
        
 ##################################################################################################################################################################
 ## Time Complexity = O (vertices + Edges)
 ## Explanation: Time complexity is this because when we are at one node then all its childerns are being explored at that time. Even though we donot visit them but
 ##              still they are being explored. Another form of looking at it is that O(v) is because we will be traversing through all nodes, but when we are at 
 ##              particular node then the length of the for loop depends on its childern which corresponds to number of edges that is O(e).
 ## Space Complexity = O (vertices)
 ## Explanation: Space complexity is this because we have to store all the vertices or nodes in the array. And also in case of worst case when we have single branch
 ##              we will be having this complexity
 ###################################################################################################################################################################
