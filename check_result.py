from check_pieces import check_piece
from chess import white_locations, black_locations, HEIGHT, WIDTH, screen, font, big_font, draw_board, draw_pieces
import pygame

def check_win():
    if (4, 0) in white_locations:
        if check_piece(4, 0) == [] and check_piece(3, 0) == [] and check_piece(5, 0) == [] and check_piece(2, 0) == [] and check_piece(6, 0) == []:
            return 'black'
    if (4, 7) in black_locations:
        if check_piece(4, 7) == [] and check_piece(3, 7) == [] and check_piece(5, 7) == [] and check_piece(2, 7) == [] and check_piece(6, 7) == []:
            return 'white'
    return 'not yet'

# Hàm xử lý khi một ván chơi kết thúc
def end(result):
    screen.fill((255, 255, 255))
    # Hiển thị thông báo chiến thắng
    if result == 'white':
        text = big_font.render('Người chơi Trắng chiến thắng!', True, (0, 0, 0))
    else:
        text = big_font.render('Người chơi Đen chiến thắng!', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()

# Hàm xử lý khi trò chơi đang diễn ra
def running_game():
    global selection, valid_moves, turn_step
    screen.fill((255, 255, 255))
    draw_board()
    draw_pieces()
    # Hiển thị lượt của người chơi
    if turn_step == 0 or turn_step == 2:
        text = font.render('Lượt người chơi Trắng', True, (0, 0, 0))
    else:
        text = font.render('Lượt người chơi Đen', True, (0, 0, 0))
    screen.blit(text, (10, 10))
    # Hiển thị quân cờ được chọn
    if selection != 100:
        pygame.draw.rect(screen, (255, 0, 0), (selection[0] * 100, selection[1] * 100, 100, 100), 4)
    # Hiển thị các nước đi hợp lệ
    for move in valid_moves:
        pygame.draw.circle(screen, (0, 255, 0), (move[0] * 100 + 50, move[1] * 100 + 50), 10)