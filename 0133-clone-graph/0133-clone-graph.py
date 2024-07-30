"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        mapping = dict()
        queue = deque([node])
        visited = set()
        start_node = None # result

        def get_cloned_graph_node(value:int):
            """Helper function to get the clone node"""
            node_exists = mapping.get(value)
            if not node_exists:
                mapping[value] = Node(val=value, neighbors=[]) # create new cloned node
            return mapping[value]

        while queue:
            element = queue.popleft()
            visited.add(element)

            # get the respective clone node, If it is not already created, create and update the mapping
            clone_node = get_cloned_graph_node(element.val)

            if not start_node:
                start_node = clone_node

            for neighbour in element.neighbors:
                if neighbour in visited:
                    continue

                queue.append(neighbour)

                # get the neighbour clone node
                neighbour_clone_node = get_cloned_graph_node(neighbour.val)

                # add undirectional linking
                clone_node.neighbors.append(neighbour_clone_node)
                neighbour_clone_node.neighbors.append(clone_node)

        return start_node
