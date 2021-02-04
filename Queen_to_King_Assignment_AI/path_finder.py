from queue import PriorityQueue
import math
import numpy as np

came_from = {}
actual_cost_from_start = {}
total_points = {}
visited_nodes = {}
visited_white_pieces = {}
# visited_black_pieces = {}
visited_pieces = {}
white_piece_positions = []
pts_multiplier = 5
pts_distance_multiplier = 3
is_king_found = False

def search_path_for_queen(piecePositions):
    grid, start_node, end_node = make_chess_grid(piecePositions)
    for p in piecePositions.items(): white_piece_positions.append(p) if (p[0][0]=='W' and p[0]!='WQ' and p[0]!='WK') else None  # Filtering out only white piece pos
    q = PriorityQueue()
    actual_cost_from_start[start_node[1]] = 0
    q.put((0, start_node[1]))
    while(not q.empty()):
        currentNodeData = q.get();
        currentNodeLocation = currentNodeData[1]
        currentNodeContent = grid[currentNodeLocation[0]][currentNodeLocation[1]]
        visited_nodes[currentNodeLocation] = True
        neighbours = get_neighbours(currentNodeLocation, grid, q, end_node)
        if is_king_found and len(visited_white_pieces) == len(white_piece_positions): 
            print('We have found our king! This is awesome!!')
            print_optimal_path(currentNodeLocation, end_node)
            return True
        print("\n----\n" , neighbours, "||||| --- visiting---", currentNodeLocation, " pts - ", total_points.get(currentNodeLocation) )
    # print_optimal_path(currentNodeLocation, end_node)

def print_optimal_path(currentNodeLocation, end_node):
    currentNode = currentNodeLocation
    optimal_path = str(currentNodeLocation)
    while(came_from.get(currentNode)!=None):
        optimal_path+=str(came_from.get(currentNode))
        currentNode = came_from.get(currentNode)
    optimal_path=str(end_node[1])+optimal_path
    print(optimal_path)

def update_points(neighbour_data, neighbour_pos, currentNodePos):
    if(visited_pieces.get(neighbour_pos)!=True):
        if neighbour_data == 'WK':
            global is_king_found
            is_king_found=True
        elif(neighbour_data[0] == 'W'):
            total_points[(neighbour_pos[0]+1, neighbour_pos[1])] = (total_points[(neighbour_pos[0]+1, neighbour_pos[1])]+1) if total_points.get((neighbour_pos[0]+1, neighbour_pos[1]))!=None else 1
            total_points[(neighbour_pos[0]-1, neighbour_pos[1])] = (total_points[(neighbour_pos[0]-1, neighbour_pos[1])]+1) if total_points.get((neighbour_pos[0]-1, neighbour_pos[1]))!=None else 1
            total_points[(neighbour_pos[0], neighbour_pos[1]+1)] = (total_points[(neighbour_pos[0], neighbour_pos[1]+1)]+1) if total_points.get((neighbour_pos[0], neighbour_pos[1]+1))!=None else 1
            total_points[(neighbour_pos[0], neighbour_pos[1]-1)] = (total_points[(neighbour_pos[0], neighbour_pos[1]-1)]+1) if total_points.get((neighbour_pos[0], neighbour_pos[1]-1))!=None else 1
            visited_white_pieces[neighbour_pos] = True
            visited_pieces[neighbour_pos] = True
        elif(neighbour_data[0] == 'B'):
            total_points[(neighbour_pos[0]+1, neighbour_pos[1])] = (total_points[(neighbour_pos[0]+1, neighbour_pos[1])]-1) if total_points.get((neighbour_pos[0]+1, neighbour_pos[1]))!=None else 0
            total_points[(neighbour_pos[0]-1, neighbour_pos[1])] = (total_points[(neighbour_pos[0]-1, neighbour_pos[1])]-1) if total_points.get((neighbour_pos[0]-1, neighbour_pos[1]))!=None else 0
            total_points[(neighbour_pos[0], neighbour_pos[1]+1)] = (total_points[(neighbour_pos[0], neighbour_pos[1]+1)]-1) if total_points.get((neighbour_pos[0], neighbour_pos[1]+1))!=None else 0
            total_points[(neighbour_pos[0], neighbour_pos[1]-1)] = (total_points[(neighbour_pos[0], neighbour_pos[1]-1)]-1) if total_points.get((neighbour_pos[0], neighbour_pos[1]-1))!=None else 0
            visited_pieces[neighbour_pos] = True
            total_points[currentNodePos] = (total_points[currentNodePos]-1) if total_points.get(currentNodePos)!=None else 0

def get_neighbours(currentNodeLocation, grid, q, end_node):
    currentNode_pos = currentNodeLocation
    neighbours = []
    if(visited_nodes.get((currentNode_pos[0]+1, currentNode_pos[1]))!=True and currentNode_pos[0]+1<8):  # Down neighbour
        if (currentNode_pos[0]+1, currentNode_pos[1]) not in piecePositions.values():   # we cannot go on an occupied position
            neighbours.append((currentNode_pos[0]+1, currentNode_pos[1]))   # Tracking actual_cost_from_start of neighbour from start
            came_from[neighbours[-1]] = currentNode_pos
            total_points[neighbours[-1]] = total_points.get(currentNode_pos) if total_points.get(currentNode_pos)!=None else 0
            # total_points[currentNode_pos] = total_points.get(came_from.get(currentNode_pos)) if total_points.get(came_from.get(currentNode_pos))!=None else 0
            actual_cost_from_start[neighbours[-1]] = actual_cost_from_start[currentNode_pos] + 1
            heuristic_cost = get_heuristic_cost(neighbours[-1], currentNode_pos, end_node)
            q.put((-heuristic_cost, neighbours[-1]))
        else:
            update_points(grid[currentNode_pos[0]+1][currentNode_pos[1]], (currentNode_pos[0]+1, currentNode_pos[1]), currentNode_pos)
            if is_king_found: 
                came_from [(currentNode_pos[0]+1, currentNode_pos[1])] = currentNode_pos          
                return neighbours

    if(visited_nodes.get((currentNode_pos[0]-1, currentNode_pos[1]))!=True and currentNode_pos[0]-1>=0): # Up neighbour
        if (currentNode_pos[0]-1, currentNode_pos[1]) not in piecePositions.values():
            neighbours.append((currentNode_pos[0]-1, currentNode_pos[1]))
            came_from[neighbours[-1]] = currentNode_pos
            total_points[neighbours[-1]] = total_points.get(currentNode_pos) if total_points.get(currentNode_pos)!=None else 0
            # total_points[currentNode_pos] = total_points.get(came_from.get(currentNode_pos)) if total_points.get(came_from.get(currentNode_pos))!=None else 0
            actual_cost_from_start[(currentNode_pos[0]-1, currentNode_pos[1])] = actual_cost_from_start[currentNode_pos] + 1
            heuristic_cost = get_heuristic_cost(neighbours[-1], currentNode_pos, end_node)
            q.put((-heuristic_cost, neighbours[-1]))
        else:
            update_points(grid[currentNode_pos[0]-1][currentNode_pos[1]], (currentNode_pos[0]-1, currentNode_pos[1]), currentNode_pos)
            if is_king_found:
                came_from [(currentNode_pos[0]-1, currentNode_pos[1])] = currentNode_pos
                return neighbours

    if(visited_nodes.get((currentNode_pos[0], currentNode_pos[1]+1))!=True and currentNode_pos[1]+1<8):  # Right neighbour
        if (currentNode_pos[0], currentNode_pos[1]+1) not in piecePositions.values():
            neighbours.append((currentNode_pos[0], currentNode_pos[1]+1))
            came_from[neighbours[-1]] = currentNode_pos
            total_points[neighbours[-1]] = total_points.get(currentNode_pos) if total_points.get(currentNode_pos)!=None else 0
            # total_points[currentNode_pos] = total_points.get(came_from.get(currentNode_pos)) if total_points.get(came_from.get(currentNode_pos))!=None else 0
            actual_cost_from_start[(currentNode_pos[0], currentNode_pos[1]+1)] = actual_cost_from_start[currentNode_pos] + 1
            heuristic_cost = get_heuristic_cost(neighbours[-1], currentNode_pos, end_node)
            q.put((-heuristic_cost, neighbours[-1]))
        else:
            update_points(grid[currentNode_pos[0]][currentNode_pos[1]+1], (currentNode_pos[0], currentNode_pos[1]+1), currentNode_pos)
            if is_king_found: 
                came_from [(currentNode_pos[0], currentNode_pos[1]+1)] = currentNode_pos
                return neighbours

    if(visited_nodes.get((currentNode_pos[0], currentNode_pos[1]-1))!=True and currentNode_pos[1]-1>=0): # Left neighbour
        if (currentNode_pos[0], currentNode_pos[1]-1) not in piecePositions.values():
            neighbours.append((currentNode_pos[0], currentNode_pos[1]-1))
            came_from[neighbours[-1]] = currentNode_pos
            total_points[neighbours[-1]] = total_points.get(currentNode_pos) if total_points.get(currentNode_pos)!=None else 0
            # total_points[currentNode_pos] = total_points.get(came_from.get(currentNode_pos)) if total_points.get(came_from.get(currentNode_pos))!=None else 0
            actual_cost_from_start[(currentNode_pos[0], currentNode_pos[1]-1)] = actual_cost_from_start[currentNode_pos] + 1
            heuristic_cost = get_heuristic_cost(neighbours[-1], currentNode_pos, end_node)
            q.put((-heuristic_cost, neighbours[-1]))
        else:
            update_points(grid[currentNode_pos[0]][currentNode_pos[1]-1], (currentNode_pos[0], currentNode_pos[1]-1), currentNode_pos)
            if is_king_found: 
                came_from [(currentNode_pos[0], currentNode_pos[1]-1)] = currentNode_pos
                return neighbours

    return neighbours

def get_heuristic_cost(neighbour_pos, current_pos, end_node):
    points_till_now = total_points.get(current_pos) if total_points.get(current_pos)!=None else 0
    distance_from_points = []
    shortest_dist_from_point= (None, 100)
    for white_piece in white_piece_positions:
        if(visited_white_pieces.get(white_piece[1])==None):
            dist =  get_euclidean_dist(neighbour_pos, white_piece[1])
            if shortest_dist_from_point==None or dist<shortest_dist_from_point[1]:
                shortest_dist_from_point = (white_piece[1], dist)
    euclidean_dist_to_goal = get_euclidean_dist(neighbour_pos, end_node[1])
    heuristic_cost = pts_multiplier*points_till_now - pts_distance_multiplier*shortest_dist_from_point[1] - actual_cost_from_start[neighbour_pos] - euclidean_dist_to_goal
    return heuristic_cost

def get_euclidean_dist(fromNode, toNode):
    x1,y1 = fromNode
    x2,y2 = toNode
    return math.sqrt(math.pow((abs(x2-x1)), 2) + math.pow((abs(y2-y1)), 2))


def make_chess_grid(piecePositions):
    grid=np.empty((8,8), dtype=tuple)
    start_node = None
    end_node = None
    for piece in piecePositions.items():
        grid[piece[1][0]] [piece[1][1]] = piece[0]
        if(piece[0]=='WQ'): start_node = ('WQ', piece[1])
        elif(piece[0]=='WK'): end_node = ('WK', piece[1])
    return grid, start_node, end_node

# Inputs - initial board position

piecePositions = {
    'WQ': (0,0),
    'WB': (2,6),
    'WR': (7,1),
    'WP': (2,1),
    'WK': (5,7),
    'BQ': (0,6),
    'BB': (5,5),
    'BR': (5,3),
    'BP': (6,4),
    'BK': (1,4),
}

search_path_for_queen(piecePositions)