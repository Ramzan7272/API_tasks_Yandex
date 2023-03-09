import pygame
import requests

PgUp_count = 0
PgDown_count = 0


def get_image(coords):
    base = f'https://static-maps.yandex.ru/1.x/?ll={coords}&spn=20,20&l=sat'
    req = requests.get(base)
    if req:
        with open('australia.png', 'wb') as f:
            f.write(req.content)


get_image('133.791467,-25.694422')
pygame.init()
size = width, height = 600, 450
screen = pygame.display.set_mode(size)
im = pygame.image.load('australia.png')
screen.blit(im, (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass