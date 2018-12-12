import pygame
import sys
import BST
import random

tree = BST.BSTMap()
for x in range(15):
    tree.add(random.randint(1, 100), random.randint(1, 100))

WIDTH, HEIGHT = 1500, 1000
CENTRE = WIDTH // 2
TOP = HEIGHT - (HEIGHT - 40)
RADIUS = 30
OFFSET = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    count = 0
    for item in tree.BFS(tree._root):
        if count == 0:
            item.x, item.y = CENTRE, TOP
        if not item.drawn:
            if item.left:
                item.left.x, item.left.y = item.x - (OFFSET // item.left.x), \
                    item.y + (40 * item.left.y)
                pygame.draw.line(screen, (255, 0, 0), (item.x, item.y),
                                 (item.left.x, item.left.y))
            if item.right:
                item.right.x, item.right.y = item.x + (OFFSET // item.right.x), \
                    item.y + (40 * item.right.y)
                pygame.draw.line(screen, (255, 0, 0), (item.x, item.y),
                                 (item.right.x, item.right.y))

            pygame.draw.circle(screen, (0, 255, 0),
                               (item.x, item.y),
                               RADIUS, 1)
            textsurface = myfont.render(str(item.key), False, (0, 0, 255))
            screen.blit(textsurface, (item.x - 15, item.y - 20))

        item.drawn = True
        count += 1
    pygame.display.update()
