import pygame
from pygame.draw import *
import random
import math

pygame.init()

nickname = input("Nickname ")

time = 10  # время длительности игры в секундах
FPS = 60
screen_width = 1400
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

score = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

file = open("top.txt", 'a')


def new_ball():  # Функция создает новый шарик случайного радиуса, случайного цвета.
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    r = random.randint(30, 50)
    color = COLORS[random.randint(0, 5)]
    circle(screen, color, (x, y), r)
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    return [x, y, r, color, dx, dy]


def click(event):  # return mouse position
    (x, y) = event.pos
    return [x, y]


def hit_ball(func_click, balls_pos):  # Функция проверяет, был ли клик внутри шара, если да, то прибавляет 1 очко
    global score
    for i in range(len(balls_pos)):
        if math.sqrt((func_click[0] - balls_pos[i][0]) ** 2 + (func_click[1] - balls_pos[i][1]) ** 2) \
                <= balls_pos[i][2]:
            del balls_pos[i]
            balls_pos.append(new_ball())
            score += 1


def score_show(score):  # Функция выводит количество очков
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Score: ' + str(score), True, (180, 0, 0))
    screen.blit(text1, (10, 50))


balls_pos = []

# Циклы добавляют параметры шаров и квадратов в массив.
for i in range(15):
    balls_pos.append(new_ball())


def move_balls(balls_pos):  # Функция перемещает шары в соответствии с их параметрами из массива.
    for i in range(len(balls_pos)):
        balls_pos[i][0] += balls_pos[i][4]
        balls_pos[i][1] += balls_pos[i][5]

        if balls_pos[i][0] + balls_pos[i][2] >= screen_width:
            balls_pos[i][0] -= balls_pos[i][4]
            balls_pos[i][4] = - balls_pos[i][4]

        if balls_pos[i][0] - balls_pos[i][2] <= 0:
            balls_pos[i][0] -= balls_pos[i][4]
            balls_pos[i][4] = - balls_pos[i][4]

        if balls_pos[i][1] + balls_pos[i][2] >= screen_height:
            balls_pos[i][1] -= balls_pos[i][5]
            balls_pos[i][5] = - balls_pos[i][5]

        if balls_pos[i][1] - balls_pos[i][2] <= 0:
            balls_pos[i][1] -= balls_pos[i][5]
            balls_pos[i][5] = - balls_pos[i][5]

        circle(screen, balls_pos[i][3], (balls_pos[i][0], balls_pos[i][1]), balls_pos[i][2])


def touch(ball1: object, ball2: object):  # функция проверяет касание шаров
    flag = False
    if (int((ball1[0] - ball2[0])) ^ 2 + int((ball1[1] - ball2[1])) ^ 2 <= int((ball1[2] + ball2[2])) ^ 2):
        flag = True
    return flag


def reflect(ball1: object, ball2: object) -> object:
    x = float(ball2[0] - ball1[0])
    y = float(ball2[1] - ball1[1])
    vx = float(ball1[4])
    vy = float(ball1[5])
    if (vx * x + vy * y > 0):
        # (vx, vy) = (vx, vy) - 2.0 * (x, y) / (x^2.0 + y ^ 2.0) * (vx * x + vy * y)
        vx = vx - 2.0 * x / ((int(x) ^ 2 + int(y) ^ 2) * (vx * x + vy * y) + 1)
        vy = vy - 2.0 * y / ((int(x) ^ 2 + int(y) ^ 2) * (vx * x + vy * y) + 1)
        if vx < 5 :
            vx = int(vx * 1.2)
            vy = int(vy * 1.2)
        vx = int(vx)
        vy = int(vy)
    ball1[4] = vx
    ball1[5] = vy
    return ball1


pygame.display.update()
clock = pygame.time.Clock()
finished = 0

while finished < time * FPS:
    clock.tick(FPS)
    print(balls_pos)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit_ball(click(event), balls_pos)
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
    score_show(score)
    move_balls(balls_pos)
    for i in range(len(balls_pos)):
        for j in range(len(balls_pos)):
            if (i != j) and (touch(ball1=balls_pos[i], ball2=balls_pos[j])):
                balls_pos[i] = reflect(ball1=balls_pos[i], ball2=balls_pos[j])

    pygame.display.update()
    screen.fill(BLACK)
    finished += 1

file.write(nickname + " " + str(score) + '\n')
file.close()
pygame.quit()

file = open('top.txt', 'r')
data = []

while True:
    a = file.readline()
    if a == "":
        break
    data.append(a)
for i in range(len(data)):
    a = data[i]
    a = a.split()
    data[i] = a

print(data)
file.close()


def sort_col(i):
    return int(i[1])


data.sort(key=sort_col)
print(data)
file.close()

file = open('top.txt', 'w')
for i in range(len(data)):
    file.write(str(data[i][0]) + " " + str(data[i][1]) + "\n")
