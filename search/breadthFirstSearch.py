# Algorithm: Breadth First Search
# Type: Searching Algorithm
# Time Complexity: O(V + E)
# Space Complexity: O(V)

# 1. Create a graph
# 2. Create a function called is_target that takes a name as an argument and returns True if the name is 'TARGET' and False otherwise
# 3. Create a function called breadth_first_search that takes a graph and a start node as arguments
# 4. Create a set called visited
# 5. Create a queue and add the start node to it
# 6. While the queue is not empty:
# 7. Remove the first node from the queue and assign it to current_node
# 8. If current_node is not in visited:
# 9. Add current_node to visited
# 10. If current_node is the target node:
# 11. Return visited
# 12. Add the neighbors of current_node to the queue
# 13. Return visited


# Create a graph with nodes and their neighbors
# The graph must have a node called 'TARGET' that is the target node
# The graph must have at least 3 nodes with no neighbors
# The graph must have multiple viable paths to the target node
# The graph must have at least 30 nodes
# The graph must have at least 3 nodes with only one neighbor
# The graph must have at least 3 nodes with more than 3 neighbors
# The graph must have at least 3 nodes with the same neighbors

graph = {
    'Alice': ['Bob', 'Claire', 'Dennis'],
    'Bob': ['Alice', 'Eve'],
    'Claire': ['Alice', 'Dennis', 'Linda'],
    'Dennis': ['Alice', 'Claire', 'Ivy'],
    'Eve': ['Bob', 'Frank', 'George'],
    'Frank': ['Eve', 'Hannah'],
    'George': ['Eve', 'Ivy'],
    'Hannah': ['Frank', 'Ivy'],
    'Ivy': ['Dennis', 'George', 'Hannah', 'Jack'],
    'Jack': ['Ivy', 'Karen', 'TARGET'],
    'Karen': ['Jack', 'TARGET'],
    'TARGET': ['Linda', 'Oscar'],
    'Linda': ['TARGET'],
    'Oscar': ['TARGET'],
    'Paul': [],  # Node with no neighbors
    'Quinn': [],  # Node with no neighbors
    'Rachel': [],  # Node with no neighbors
    'Sam': ['Tom'],  # Node with only one neighbor
    'Tom': ['Sam', 'Uma'],  # Node with only one neighbor
    'Uma': ['Tom'],  # Node with only one neighbor
    'Victor': ['Wendy', 'Xander', 'Yara'],
    'Wendy': ['Victor', 'Xander', 'Yara'],
    'Xander': ['Victor', 'Wendy', 'Yara'],
    'Yara': ['Victor', 'Wendy', 'Xander']
}


def is_target(name):
    return name == 'TARGET'


def breadth_first_search(graph, start):
    visited = set()
    queue = [start]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.add(current_node)
            if is_target(current_node):
                return "Target found for " + start
            queue.extend(graph[current_node])
    return "Target not found for " + start


# Reaching the target node from Alice
print(breadth_first_search(graph, 'Alice'))

# Not reaching the target node from Quinn
print(breadth_first_search(graph, 'Quinn'))

# Reaching the target node from George
print(breadth_first_search(graph, 'George'))

# Not reaching the target node from Rachel
print(breadth_first_search(graph, 'Rachel'))
