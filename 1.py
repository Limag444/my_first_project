import pygame
import os
import sys
from random import shuffle

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('C:\\Users\\student\\PycharmProjects\\ostrov_sokrovisch\\data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    size = width, height = 0, 0
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Остров сокровищ')
    sprite2 = pygame.sprite.Sprite()
    all_sprites = pygame.sprite.Group()
    zastavka = load_image('заставка.png')
    tzastavka = pygame.transform.scale(zastavka, (1350, 775))
    sprite2.image = tzastavka
    sprite2.rect = sprite2.image.get_rect()
    all_sprites.add(sprite2)
    all_sprites.draw(screen)
    pygame.display.flip()
    zas = True
    while zas:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                zas = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                zas = False
    sprite2.kill()

    pygame.quit()
