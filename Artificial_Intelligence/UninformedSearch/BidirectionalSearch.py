from Graph import Graph

def bidirectionalSearch(graph, startingNode, goalNode):
    start_queue = [(startingNode, 0)]
    goal_queue = [(goalNode, 0)]
    visited_start = []
    visited_goal = []
    came_from_start = {}
    came_from_goal = {}
    while(len(start_queue)>0 and len(goal_queue)>0):
        current_node_start = start_queue.pop()
        current_node_goal = goal_queue.pop()
        visited_start.append(current_node_start[0])
        visited_goal.append(current_node_goal[0])
        neighbours_start = edges.get(current_node_start[0])
        neighbours_goal = edges.get(current_node_goal[0])
        if current_node_start == current_node_goal:
            reconstruct_path(current_node_goal, came_from_start, came_from_goal, startingNode, goalNode)
        for neighbour_start in neighbours_start:
            if neighbour_start[0] not in visited_start:
                came_from_start[neighbour_start[0]] = current_node_start
                start_queue.append(neighbour_start)
        for neighbour_goal in neighbours_goal:
            if neighbour_goal[0] not in visited_goal:
                came_from_goal[neighbour_goal[0]] = current_node_goal
                goal_queue.append(neighbour_goal)
                if is_meeting_neighbour(neighbour_goal, neighbours_start) or neighbour_goal[0] == current_node_start[0]:
                    print("Meeting point found", neighbour_goal)
                    reconstruct_path(neighbour_goal, came_from_start, came_from_goal, startingNode, goalNode)
                    return

def is_meeting_neighbour(neighbour_goal, neighbours_start):
    for elm in neighbours_start:
        if elm[0] == neighbour_goal[0]:
            return True
    return False

def reconstruct_path(meeting_node, came_from_start, came_from_goal, startingNode, goalNode):
    node = meeting_node
    start_path = ""
    goal_path = ""
    while(came_from_start.get(node[0])!=None):
        start_path+=came_from_start.get(node[0])[0]
        if node == startingNode:
            break
        node = came_from_start.get(node[0])
    node = meeting_node
    start_path = start_path[::-1]+ meeting_node[0]
    while(came_from_goal.get(node[0])!=None):
        goal_path+=came_from_goal.get(node[0])[0]
        if node == goalNode:
            break
        node = came_from_goal.get(node[0])
    
    print("Starting path = ", start_path)
    print("Goal path = ", goal_path)
    print("FinalPath = ", start_path + goal_path)
    
nodes = ['S', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
edges = {
    'S': [('B',4), ('C',3)],
    'B': [('E',12), ('F', 5), ('S', 4)],
    'C': [('D',7), ('E',10), ('S', 3)],
    'D': [('E',2), ('C', 7), ('H', 4), ('I', 3)],
    'E': [('G',5), ('B', 12), ('C', 10), ('D', 2)],
    'F': [('G',16), ('B', 5)],
    'G': [('E', 5), ('F', 16), ('H', 5)],
    'H': [('D', 4), ('G', 5)],
    'I': [('D', 3)]
    }


graph = Graph(nodes, edges)
bidirectionalSearch(graph, 'S', 'H')