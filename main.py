import pygame
import sys
from log import *
from database import get_best, cur, insert_result

GAMERS_DB = get_best()


def draw_top_gamers():
    font_top = pygame.font.SysFont("sismun", 30)
    font_gamer = pygame.font.SysFont("sismun", 24)
    text_head = font_top.render("Best tries: ", True, COLOR_TEXT)
    screen.blit(text_head, (250, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        print(index, name, score)
        s = f"{index + 1}.{name} - {score}"
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (250, 30 + 30 * index))
        print(index, name, score)


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("sismun", 48)
    font_delta = pygame.font.SysFont("sismun", 32)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, COLOR_TEXT)
        screen.blit(text_delta, (170, 65))
    pretyy_print(mas)
    draw_top_gamers()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + 110
            pygame.draw.rect(screen, COLORS[value], (w, h, 110, 110))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))




COLOR_TEXT = (255, 127, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (225, 225, 255),
    32: (225, 225, 128),
    64: (225, 225, 0),
    128: (255, 225, 0)
}

WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)

def init_const():
    score, mas
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    mas = insert_2_or_4(mas, x1, y1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x2, y2)
    score = 0

mas = None
score = None
init_const()
USERNAME = None


print(get_empty_list(mas))
pretyy_print(mas)

# for gamer in get_best():
# print(gamer)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def draw_intro():
    img2048 = pygame.image.load('img.png')
    font = pygame.font.SysFont("stxingkai", 70)
    text_welcome = font.render("Welcome! ", True, WHITE)
    name = 'Введите имя'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Введите имя':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_welcome, (230, 80))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def draw_game_over():
    USERNAME, mas, score
    img2048 = pygame.image.load('img.png')
    font = pygame.font.SysFont("stxingkai", 65)
    text_game_over = font.render("Game over! ", True, WHITE)
    text_score = font.render(f"Вы набрали {score}", True, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = "Рекрорд побит"
    else:
        text = f"Рекорд {best_score}"
    text_record = font.render(text, True, WHITE)
    insert_result(USERNAME, score)
    make_disicion = False
    while not make_disicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #restart game with name
                    make_disicion = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    # restart game without name
                    USERNAME = None
                    make_disicion = True
                    init_const()
        screen.fill(BLACK)
        screen.blit(text_game_over, (220, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        pygame.display.update()
    screen.fill(BLACK)


def game_loop():
    gmas, score
    draw_interface(score)
    pygame.display.update()
    is_btn_click = False
    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta = move_left(mas)
                    is_btn_click = True
                elif event.key == pygame.K_RIGHT:
                    mas, delta = move_right(mas)
                    is_btn_click = True
                elif event.key == pygame.K_UP:
                    mas, delta = move_up(mas)
                    is_btn_click = True
                elif event.key == pygame.K_DOWN:
                    mas, delta = move_down(mas)
                    is_btn_click = True
                score += delta

                if is_zero_in_mas(mas):
                    empty = get_empty_list(mas) #берем список пустых элементов
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                    print(f'Мы заполнили элемент под номером {random_num}')

                draw_interface(score, delta)
                pygame.display.update()

        print(USERNAME)
while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_game_over()
