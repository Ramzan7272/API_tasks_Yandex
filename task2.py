import pygame
import requests

PgUp_count = 600
PgDown_count = 450

def get_image(coords):
    base = f'https://static-maps.yandex.ru/1.x/?ll={coords}&spn=20,20&l=sat'
    req = requests.get(base)
    if req:
        with open('australia.png', 'wb') as f:
            f.write(req.content)

get_image('133.791467,-25.694422')

def cart():
    size = width, height = 600, 450
    screen = pygame.display.set_mode(size)
    im = pygame.image.load('australia.png')
    im1 = pygame.transform.scale(im, (PgUp_count, PgDown_count))
    screen.blit(im1, (0, 0))
    pygame.display.flip()

pygame.init()
cart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                PgUp_count += 5
                PgDown_count += 5
                cart()
            elif event.key == pygame.K_PAGEDOWN:
                PgDown_count -= 5
                PgUp_count -= 5
                cart()