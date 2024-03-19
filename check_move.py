from chess import white_locations, black_locations

def check_queen_move(x, y):
    queen_moves = []
    step = 1
    while x + step < 8 and y + step < 8:
        if (x + step, y + step) in white_locations:
            break
        queen_moves.append((x + step, y + step))
        if (x + step, y + step) in black_locations:
            break
        step += 1
    step = 1
    while x + step < 8 and y - step >= 0:
        if (x + step, y - step) in white_locations:
            break
        queen_moves.append((x + step, y - step))
        if (x + step, y - step) in black_locations:
            break
        step += 1
    step = 1
    while x - step >= 0 and y + step < 8:
        if (x - step, y + step) in white_locations:
            break
        queen_moves.append((x - step, y + step))
        if (x - step, y + step) in black_locations:
            break
        step += 1
    step = 1
    while x - step >= 0 and y - step >= 0:
        if (x - step, y - step) in white_locations:
            break
        queen_moves.append((x - step, y - step))
        if (x - step, y - step) in black_locations:
            break
        step += 1
    step = 1
    while x + step < 8:
        if (x + step, y) in white_locations:
            break
        queen_moves.append((x + step, y))
        if (x + step, y) in black_locations:
            break
        step += 1
    step = 1
    while x - step >= 0:
        if (x - step, y) in white_locations:
            break
        queen_moves.append((x - step, y))
        if (x - step, y) in black_locations:
            break
        step += 1
    step = 1
    while y + step < 8:
        if (x, y + step) in white_locations:
            break
        queen_moves.append((x, y + step))
        if (x, y + step) in black_locations:
            break
        step += 1
    step = 1
    while y - step >= 0:
        if (x, y - step) in white_locations:
            break
        queen_moves.append((x, y - step))
        if (x, y - step) in black_locations:
            break
        step += 1
    return queen_moves
def check_king_move(x, y):
    king_moves = []
    if x - 1 >= 0:
        king_moves.append((x - 1, y))
    if x + 1 < 8:
        king_moves.append((x + 1, y))
    if y - 1 >= 0:
        king_moves.append((x, y - 1))
    if y + 1 < 8:
        king_moves.append((x, y + 1))
    if x + 1 < 8 and y + 1 < 8:
        king_moves.append((x + 1, y + 1))
    if x - 1 >= 0 and y - 1 >= 0:
        king_moves.append((x - 1, y - 1))
    if x - 1 >= 0 and y + 1 < 8:
        king_moves.append((x - 1, y + 1))
    if x + 1 < 8 and y - 1 >= 0:
        king_moves.append((x + 1, y - 1))
    return king_moves

def check_rook_move(x, y):
    rook_moves = []
    c = 1
    while x + c < 8:
        if (x + c, y) in white_locations:
            break
        rook_moves.append((x + c, y))
        if (x + c, y) in black_locations:
            break
        c += 1
    c = 1
    while x - c >= 0:
        if (x - c, y) in white_locations:
            break
        rook_moves.append((x - c, y))
        if (x - c, y) in black_locations:
            break
        c += 1
    c = 1
    while y + c < 8:
        if (x, y + c) in white_locations:
            break
        rook_moves.append((x, y + c))
        if (x, y + c) in black_locations:
            break
        c += 1
    c = 1
    while y - c >= 0:
        if (x, y - c) in white_locations:
            break
        rook_moves.append((x, y - c))
        if (x, y - c) in black_locations:
            break
        c += 1
    return rook_moves

def check_bishop_move(x, y):
    bishop_moves = []
    if x + 1 < 8 and y + 1 < 8:
        bishop_moves.append((x + 1, y + 1))
    if x - 1 >= 0 and y + 1 < 8:
        bishop_moves.append((x - 1, y + 1))
    if x + 1 < 8 and y - 1 >= 0:
        bishop_moves.append((x + 1, y - 1))
    if x - 1 >= 0 and y - 1 >= 0:
        bishop_moves.append((x - 1, y - 1))
    return bishop_moves

def check_knight_move(x, y):
    knight_moves = []
    if x + 2 < 8 and y + 1 < 8:
        knight_moves.append((x + 2, y + 1))
    if x - 2 >= 0 and y + 1 < 8:
        knight_moves.append((x - 2, y + 1))
    if x + 2 < 8 and y - 1 >= 0:
        knight_moves.append((x + 2, y - 1))
    if x - 2 >= 0 and y - 1 >= 0:
        knight_moves.append((x - 2, y - 1))
    if x + 1 < 8 and y + 2 < 8:
        knight_moves.append((x + 1, y + 2))
    if x - 1 >= 0 and y + 2 < 8:
        knight_moves.append((x - 1, y + 2))
    if x + 1 < 8 and y - 2 >= 0:
        knight_moves.append((x + 1, y - 2))
    if x - 1 >= 0 and y - 2 >= 0:
        knight_moves.append((x - 1, y - 2))
    return knight_moves

def check_pawn_move(x, y, color):
    if color == 'white':
        if (x, y - 1) not in black_locations and (x, y - 1) not in white_locations:
            pawn_moves = [(x, y - 1)]
        else:
            pawn_moves = []
        if y == 6 and (x, y - 1) not in black_locations and (x, y - 1) not in white_locations and (x, y - 2) not in black_locations and (x, y - 2) not in white_locations:
            pawn_moves.append((x, y - 2))
    else:
        if (x, y + 1) not in black_locations and (x, y + 1) not in white_locations:
            pawn_moves = [(x, y + 1)]
        else:
            pawn_moves = []
        if y == 1 and (x, y + 1) not in black_locations and (x, y + 1) not in white_locations and (x, y + 2) not in black_locations and (x, y + 2) not in white_locations:
            pawn_moves.append((x, y + 2))
    return pawn_moves