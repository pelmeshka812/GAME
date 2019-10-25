import pygame

pygame.init()
pygame.display.set_caption("Simple game")
sc = pygame.display.set_mode((500, 500))
GREEN = (0, 160, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
W = 500 # ширина и высота основного окна
H = 500
x = 50 # координаты прямоугольника, который прыгает
y = 300
width = 40 # ширина и высота прямоугольника, который прыгает
height = 60
RECT_WIDTH = 30 #ширина и высота препятсвий
RECT_HEIGHT = 60
speed = 5
jumpCount = 10
isJump = False

left = False
right = False
clock = pygame.time.Clock()
run = True
level_up = ["|____|____|___|_______|__|___|", "____|____|___|"] # определяет количество и частоту препятствий


def draw_window():
    sc.blit(sc, (0, 0))
    pygame.draw.rect(sc, GREEN, (x, y, width, height))
    pygame.draw.line(sc, BLUE, [0, 300 + height], [500, 300 + height], 10)
    pygame.display.update()
    sc.fill(BLACK)


def draw_barrier():# рисуем препятствия
    xR = 400
    yR = 300 + height - RECT_HEIGHT
    x_helper = 490
    for row in level_up:
        for col in row:
            if col == "|":
                while x_helper > 0:
                    pygame.draw.rect(sc, RED, (x_helper, yR, RECT_WIDTH, RECT_HEIGHT))
                    x_helper -= 10

            xR += RECT_WIDTH


while run: # основной цикл
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < W - width - speed:
        x += speed
    if not isJump: #прыжок
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount**2)/2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if keys[pygame.K_SPACE]:
        isJump = True

    clock.tick(50)
    draw_window()
    draw_barrier()

    clock.tick(50)

pygame.quit()
