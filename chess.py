import pygame
from pygame.locals import *
from check_result import check_win, end, running_game
# thiết lập chung cho game
WIDTH = 800
HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Cờ king")
font = pygame.font.SysFont(None, 20)
medium_font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 20)
timer = pygame.time.Clock()
fps = 60

# thiết lập quân cờ
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []
file_path = "D:\Studying\Python\mychess"
white_king_image = pygame.transform.scale(pygame.image.load(file_path + '\image\white\white_king.png'), (45, 45))
white_queen_image = pygame.transform.scale(pygame.image.load(file_path + '\image\white\white_queen.png'), (45, 45))
white_bishop_image = pygame.transform.scale(pygame.image.load(file_path + '\image\white\white_bishop.png'), (45, 45))
white_knight_image = pygame.transform.scale(pygame.image.load(file_path + '\image\white\white_knight.png'), (45, 45))
white_rook_image = pygame.transform.scale(pygame.image.load(file_path + '\image\white\white_rook.png'), (45, 45))
white_pawn_image = pygame.transform.scale(pygame.image.load(file_path + '\image\white\white_pawn.png'), (45, 45))
black_king_image = pygame.transform.scale(pygame.image.load(file_path + '\image\\black\\black_king.png'), (45, 45))
black_queen_image = pygame.transform.scale(pygame.image.load(file_path + '\image\\black\\black_queen.png'), (45, 45))
black_bishop_image = pygame.transform.scale(pygame.image.load(file_path + '\image\\black\\black_bishop.png'), (45, 45))
black_knight_image = pygame.transform.scale(pygame.image.load(file_path + '\image\\black\\black_knight.png'), (45, 45))
black_rook_image = pygame.transform.scale(pygame.image.load(file_path + '\image\\black\\black_rook.png'), (45, 45))
black_pawn_image = pygame.transform.scale(pygame.image.load(file_path + '\image\\black\\black_pawn.png'), (45, 45))
board = pygame.transform.scale(pygame.image.load(file_path + '\image\\board.jpg'), (800, 800))
def draw_board():
    screen.blit(board, (0, 0))
def draw_pieces():
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'king':
            screen.blit(white_king_image, white_locations[i][0] * 100, white_locations[i][1] * 100)
        if white_pieces[i] == 'queen':
            screen.blit(white_queen_image, white_locations[i][0] * 100, white_locations[i][1] * 100)
        if white_pieces[i] == 'bishop':
            screen.blit(white_bishop_image, white_locations[i][0] * 100, white_locations[i][1] * 100)
        if white_pieces[i] == 'knight':
            screen.blit(white_knight_image, white_locations[i][0] * 100, white_locations[i][1] * 100)
        if white_pieces[i] == 'rook':
            screen.blit(white_rook_image, white_locations[i][0] * 100, white_locations[i][1] * 100)
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn_image, white_locations[i][0] * 100, white_locations[i][1] * 100)
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'king':
            screen.blit(black_king_image, black_locations[i][0] * 100, black_locations[i][1] * 100)
        if black_pieces[i] == 'queen':
            screen.blit(black_queen_image, black_locations[i][0] * 100, black_locations[i][1] * 100)
        if black_pieces[i] == 'bishop':
            screen.blit(black_bishop_image, black_locations[i][0] * 100, black_locations[i][1] * 100)
        if black_pieces[i] == 'knight':
            screen.blit(black_knight_image, black_locations[i][0] * 100, black_locations[i][1] * 100)
        if black_pieces[i] == 'rook':
            screen.blit(black_rook_image, black_locations[i][0] * 100, black_locations[i][1] * 100)
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn_image, black_locations[i][0] * 100, black_locations[i][1] * 100)

def play_chess():
    global selection, valid_moves, turn_step, captured_pieces_white, captured_pieces_black, color
    color = 'white'
    state = 'not yet'
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if turn_step == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = x // 100
                    y = y // 100
                    for i in range(len(white_locations)):
                        if white_locations[i] == (x, y):
                            selection = (x, y)
                            valid_moves = check_piece(x, y)
                            turn_step = 1
                            break
            elif turn_step == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = x // 100
                    y = y // 100

                    if check_in_enemy(x, y, 'white'):
                        valid_moves = []
                        selection = 100
                        turn_step = 2
                        continue

                    if check_valid_location(x, y, valid_moves):
                        for i in range(len(white_locations)):
                            if white_locations[i] == selection:
                                if white_pieces[i] != 'pawn' and x == 0 and color == 'white':
                                    captured_pieces_black.append(black_pieces[i])
                                if white_pieces[i] != 'pawn' and x == 7 and color == 'white':
                                    captured_pieces_black.append(black_pieces[i])
                                if white_pieces[i] == 'king':
                                    king_index = i
                                white_locations[i] = (x, y)
                        selection = 100
                        valid_moves = []
                        # Kiểm tra thắng thua
                        state = check_win()
                        if state != 'not yet':
                            end(state)
                        turn_step = 2
            elif turn_step == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = x // 100
                    y = y // 100
                    for i in range(len(black_locations)):
                        if black_locations[i] == (x, y):
                            selection = (x, y)
                            valid_moves = check_piece(x, y)
                            turn_step = 3
                            break
            elif turn_step == 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = x // 100
                    y = y // 100
                    if check_in_enemy(x, y, 'black'):
                        valid_moves = []
                        selection = 100
                        turn_step = 0
                        continue
                    if check_valid_location(x, y, valid_moves):
                        for i in range(len(black_locations)):
                            if black_locations[i] == selection:
                                if black_pieces[i] != 'pawn' and x == 0 and color == 'black':
                                    captured_pieces_white.append(white_pieces[i])
                                if black_pieces[i] != 'pawn' and x == 7 and color == 'black':
                                    captured_pieces_white.append(white_pieces[i])
                                if black_pieces[i] == 'king':
                                    king_index = i
                                black_locations[i] = (x, y)
                        selection = 100
                        valid_moves = []
                        # Kiểm tra thắng thua
                        state = check_win()
                        if state != 'not yet':
                            end(state)
                        turn_step = 0

running_game()
pygame.display.update()
play_chess()
timer.tick(fps)