squares_per_side = 8

# move options are the (row, col) coordinate offsets for a possible move
move_options = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)]


def square_to_coord(square):
    row = int(square/squares_per_side)
    col = square % squares_per_side
    return (row, col)


def coord_to_square(coord):
    row = coord[0]
    col = coord[1]
    return squares_per_side * row + col


def new_coord(start_coord, move_offset):
    return (start_coord[0] + move_offset[0], start_coord[1] + move_offset[1])


def validate_position(coord):
    if 0 <= coord[0] < squares_per_side and 0 <= coord[1] < squares_per_side:
        return True
    else:
        return False

# given a single coordinate, return a list of all valid destination coordinates


def generate_target_moves(start_coord):
    all_moves = [new_coord(start_coord, x) for x in move_options]
    valid_moves = list(filter(validate_position, all_moves))
    return (valid_moves)

# given a single path, generate a list of possible paths based on move to options


def possible_paths(current_path, move_to_options):
    new_paths = []
    p = current_path
    for m in move_to_options:
        new_path = p.copy()
        new_path.append(m)
        new_paths.append(new_path)

    return (new_paths)

# a path is a list of coordinates visited in sequence
# next_path copies the current path and appends the next coordinate


def next_path(current_path, next_coord):
    new_path = current_path.copy()
    new_path.append(next_coord)
    return new_path

# translate a path of coordinates to a path of square numbers
# (useful for logging and readability)


def coord_path_to_square_path(coord_path):
    square_path = []
    for coord in coord_path:
        square_path.append(coord_to_square(coord))

    return(square_path)

# translate a list of coordinate paths to a list of square number paths


def coord_paths_to_square_paths(coord_path_list):
    square_paths = []

    for coord_path in coord_path_list:
        square_path = coord_path_to_square_path(coord_path)
        if square_path:
            square_paths.append(square_path)

    return (square_paths)

# test if the coordinate has already been visited in the path


def visited_filter(coord, visited_coords):
    if coord in visited_coords:
        return True
    else:
        return False

# given a single path, generate a list of paths to explore
# from the last node in the path


def generate_paths_to_explore(path):
    possible_coords = generate_target_moves(path[-1])

    # filter out coordinates already visited in this path
    unvisited_coords = list(
        filter(lambda coord: coord not in path, possible_coords))
    print(
        f'unvisited_coords: {list(map(lambda coord: coord_to_square(coord), unvisited_coords))}')

    # build list of new paths to explore
    new_paths = possible_paths(path, unvisited_coords)

    return(new_paths)

# recursive function that evaluates a list of paths to see if the solution has been reached
# if not, generates new paths to explore and calls itself
# while tracking the number of moves required


def explore_paths(move_number, dest_coord, current_paths, solutions):

    next_paths = []

    print(
        f'move: {move_number} exploring paths: {coord_paths_to_square_paths(current_paths)}')

    for p in current_paths:

        print(f'evaluating path: {coord_path_to_square_path(p)}')

        # last element in path is the current coordinate
        current_coord = p[-1]
        #print(f'evaluating square: {coord_to_square(current_coord)}')

        if current_coord == dest_coord:
            # add path as a solution
            print(f'*** Found a solution!: {coord_path_to_square_path(p)}')
            solutions.append(p)
            return(move_number)
        else:
            new_paths = generate_paths_to_explore(p)
            if new_paths:
                next_paths.extend(new_paths)

    # continue exploring if there's more paths and still looking for solution
    if not solutions and next_paths:
        move_number += 1
        return(explore_paths(move_number, dest_coord, next_paths, solutions))

# ---------------------------------------------------
# This is the main program used to evaluate inputs
# and search for a solution
#
# Inputs:
# ---------------------------
# src  - source square number
# dest - dest square number
# ---------------------------------------------------


def solution(src, dest):
    src_coord = square_to_coord(src)
    dest_coord = square_to_coord(dest)

    print(f'src : {src} {src_coord}')
    print(f'dest: {dest} {dest_coord}')

    initial_paths = [[src_coord]]
    solutions = []
    move_number = 0

    solution_steps = explore_paths(
        move_number, dest_coord, initial_paths, solutions)

    final_solutions = coord_paths_to_square_paths(solutions)
    print(f'square solutions: {final_solutions}')

    path_lengths = list(map(lambda s: len(s), solutions))
    print(f'path lengths: {path_lengths}')

    return (solution_steps)


#print(f'solved in: {solution(19,36)} step(s)')
#print(f'solved in: {solution(0,1)} step(s)')
