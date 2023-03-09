import pygame
import requests

PgUp_count = 600
PgDown_count = 450
x = 0
y = 0
def get_image(coords):
    base = f'https://static-maps.yandex.ru/1.x/?ll={coords}&spn=20,20&l=sat'
    req = requests.get(base)
    if req:
        with open('australia.png', 'wb') as f:
            f.write(req.content)


def cart():
    get_image(f'{x},{y}')
    size = width, height = 600, 450
    screen = pygame.display.set_mode(size)
    im = pygame.image.load('australia.png')
    im1 = pygame.transform.scale(im, (PgUp_count, PgDown_count))
    screen.blit(im1, (0, 0))
    pygame.display.flip()

pygame.init()
cart()

while True:
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= 3
        cart()
    if key[pygame.K_RIGHT]:
        x += 3
        cart()
    if key[pygame.K_UP]:
        y += 3
        cart()
    if key[pygame.K_DOWN]:
        y -= 3
        cart()
    if key[pygame.K_PAGEDOWN]:
        PgDown_count -= 5
        PgUp_count -= 5
        cart()
    if key[pygame.K_PAGEUP]:
        PgUp_count += 5
        PgDown_count += 5
        cart()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
