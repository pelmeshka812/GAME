import pygame

pygame.init()
sc = pygame.display.set_mode((500, 500))
GREEN = (0, 160, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
W = 500
H = 500
x = 50
y = 300
width = 40
height = 60
RECT_WIDTH = 30
RECT_HEIGHT = 60
speed = 5
jumpCount = 10
isJump = False

left = False
right = False
animCount = 0
clock = pygame.time.Clock()
run = True
level_1 = ["|____|____|___|_______|__|___|", "____|____|___|"]


def drawWindow(level_1):
    sc.blit(sc, (0, 0))
    global animCount
    pygame.draw.rect(sc, GREEN, (x, y, width, height))
    pygame.draw.line(sc, BLUE, [0, 300 + height], [500, 300 + height], 10)
    pygame.display.update()
    sc.fill(BLACK)
    xR = 400
    yR = 300 + height - RECT_HEIGHT
    for row in level_1:
        for col in row:  # каждый символ
            if col == "|":
                pygame.draw.rect(sc, RED, (xR, yR, RECT_WIDTH, RECT_HEIGHT))

            xR += RECT_WIDTH  # блоки платформы ставятся на ширине блоков
        xR = 0


while run:
    clock.tick(50)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < W - width - speed:
        x += speed
    if not isJump:
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

    clock.tick(100)
    drawWindow(level_1)

pygame.quit()
