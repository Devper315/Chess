from check_move import check_bishop_move, check_king_move, check_knight_move, check_pawn_move, check_queen_move, check_rook_move
from chess import white_locations, black_locations, white_pieces, black_pieces

def check_piece(x, y):
    for i in range(len(white_locations)):
        if white_locations[i] == (x, y):
            if white_pieces[i] == 'queen':
                return check_queen_move(x, y)
            if white_pieces[i] == 'king':
                return check_king_move(x, y)
            if white_pieces[i] == 'rook':
                return check_rook_move(x, y)
            if white_pieces[i] == 'bishop':
                return check_bishop_move(x, y)
            if white_pieces[i] == 'knight':
                return check_knight_move(x, y)
            if white_pieces[i] == 'pawn':
                return check_pawn_move(x, y, 'white')
            
    for i in range(len(black_locations)):
        if black_locations[i] == (x, y):
            if black_pieces[i] == 'queen':
                return check_queen_move(x, y)
            if black_pieces[i] == 'king':
                return check_king_move(x, y)
            if black_pieces[i] == 'rook':
                return check_rook_move(x, y)
            if black_pieces[i] == 'bishop':
                return check_bishop_move(x, y)
            if black_pieces[i] == 'knight':
                return check_knight_move(x, y)
            if black_pieces[i] == 'pawn':
                return check_pawn_move(x, y, 'black')
    return []
# Kiểm tra xem vị trí (x, y) có nằm trong danh sách các vị trí hợp lệ không
def check_valid_location(x, y, valid_locations):
    for i in range(len(valid_locations)):
        if (x, y) == valid_locations[i]:
            return True
    return False

# Kiểm tra xem vị trí (x, y) có nằm trong danh sách các vị trí địch không
def check_in_enemy(x, y, color):
    if color == 'white':
        for i in range(len(black_locations)):
            if (x, y) == black_locations[i]:
                return True
    else:
        for i in range(len(white_locations)):
            if (x, y) == white_locations[i]:
                return True
    return False