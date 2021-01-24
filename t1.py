import pygame
import sys
h=402               #высота
w=600              #ширина
pygame.init()
screen = pygame.display.set_mode((w,h))
fl = pygame.Rect(0, 0,w,188)
fc = (161, 245, 255)
sl = pygame.Rect(0,188,w,92)
sc = (68, 35, 223)
tl = pygame.Rect(0,188+92,w, h - 188-92)
tc= (238, 246, 12)
pygame.draw.rect(screen,fc,fl, 0)
pygame.draw.rect(screen,sc,sl, 0)
pygame.draw.rect(screen,tc,tl, 0)
shc = (186, 80, 5)
# хвост кораблика
pygame.draw.circle(screen,shc,(352,206),27)
# закрашивание ненужной части
cor= pygame.Rect(0, 0,w,206)
pygame.draw.rect(screen,sc,cor, 0)
pygame.draw.rect(screen,fc,fl, 0)
#тело кораблика
b2_sh= pygame.Rect(352,206,143,27)
pygame.draw.rect(screen,shc,b2_sh,0)
#нос кораблика
points = ((495,206), (559,206), (495,233))
pygame.draw.polygon(screen, shc, points, width=0)
# илюминатор
pygame.draw.circle(screen, (255, 255, 255), (501, 218), 8, width=0)
pygame.draw.circle(screen, (0, 0, 0), (501, 218), 8, width=2)
# мачта 408,206 - 408,111
pygame.draw.line(screen,(0, 0, 0),(408,206),(408,111),width=8)
# парус
points=((410,202), (428,157), (410,111), (466,157))
sc=(222, 213, 153)
pygame.draw.polygon(screen,sc, points, width=0)
pygame.draw.polygon(screen,(165, 175, 140), points, width=2)
pygame.draw.line(screen, (173, 166, 119), (428,157), (466,157), width=1)
pygame.draw.line(screen,(0, 0, 0),(408,206),(408,111),width=8)

# солнце
sun_c = (255, 247, 29)
sun_p = (532,54)
pygame.draw.circle(screen,sun_c,sun_p,36, width=0)
#облака
сс = (255, 255, 255)
cr = 14
positions = [(132,44), (152,44), (169,45), (120,57), (137,59), (159,59), (177,59)]
for i in (1, 2, 4, 5, 6, 3, 7):
    pygame.draw.circle(screen,(255, 255, 255),(positions[i-1][0],(positions[i-1][1])),cr, width=0)
    pygame.draw.circle(screen,(184, 184, 184),(positions[i-1][0],(positions[i-1][1])),cr, width=1)

#зонт
positions = [(92,234), (98,234), (27,263),
            (43,263), (64,263), (82,263),
            (109,263), (129,263), (149,263), (161,243)]
p1=((92,234), (98,234), (161,263), (27,263))
zc = (244, 81, 81)
pygame.draw.polygon(screen,zc, p1, width=0)
pygame.draw.line(screen, (227, 130, 25),(95,263),(95, 382),width=6)
for j in (1,2):
    if j ==1 :
        for i in (3, 4, 5, 6):
            pygame.draw.line(screen, (182, 60, 60),
                         (positions[j-1][0],(positions[j][1])),
                         (positions[i-1][0],(positions[i-1][1])),width=1)
    else:
        for i in (7, 8, 9,):
            pygame.draw.line(screen, (182, 60, 60),
                     (positions[j-1][0],(positions[j-1][1])),
                     (positions[i-1][0],(positions[i-1][1])),width=1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
