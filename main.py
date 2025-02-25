import pygame
import os
import sys
from random import shuffle

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('C:\\Users\\student\\PycharmProjects\\ostrov_sokrovich\\data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Karta:
    def __init__(self, points):
        self.points = points

    def get_points(self):
        return self.points

    def __eq__(self, other):
        return type(self) == type(other)


class Pistol(Karta):
    def __init__(self, points):
        super(Pistol, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('пистоль\\пистоль' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Popugai(Karta):
    def __init__(self, points):
        super(Popugai, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('попугай\\попугай' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Mech(Karta):
    def __init__(self, points):
        super(Mech, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('меч\\меч' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Sunduk(Karta):
    def __init__(self, points):
        super(Sunduk, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('сундук\\сундук' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Kluch(Karta):
    def __init__(self, points):
        super(Kluch, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('ключ\\ключ' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Svecha(Karta):
    def __init__(self, points):
        super(Svecha, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('свеча\\свеча' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Shturval(Karta):
    def __init__(self, points):
        super(Shturval, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('штурвал\\штурвал' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Kompas(Karta):
    def __init__(self, points):
        super(Kompas, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('компас\\компас' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Yakor(Karta):
    def __init__(self, points):
        super(Yakor, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('якорь\\якорь' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Rom(Karta):
    def __init__(self, points):
        super(Rom, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('ром\\ром' + str(points) + '.png'), (140, 200))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


def check(gz):
    for i in gz[0:-1]:
        if i == gz[-1]:
            return True
    return False


bita = list()

koloda = [Rom(i) for i in range(2, 8)]
koloda += [Kompas(i) for i in range(2, 8)]
koloda += [Yakor(i) for i in range(2, 8)]
koloda += [Pistol(i) for i in range(2, 8)]
koloda += [Popugai(i) for i in range(4, 10)]
koloda += [Svecha(i) for i in range(2, 8)]
koloda += [Shturval(i) for i in range(2, 8)]
koloda += [Kluch(i) for i in range(2, 8)]
koloda += [Sunduk(i) for i in range(2, 8)]
koloda += [Mech(i) for i in range(2, 8)]
shuffle(koloda)
first_player = []
second_player = []
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
    screen.fill(pygame.Color('yellow'))
    karta = load_image('колода.png')
    karta1 = pygame.transform.scale(karta, (180, 200))
    sprite = pygame.sprite.Sprite()
    sprite.image = karta1
    sprite.rect = sprite.image.get_rect()
    # добавим спрайт в группу
    all_sprites.add(sprite)
    sprite.rect.x = 20
    sprite.rect.y = 250
    all_sprites.draw(screen)
    running = True
    pygame.display.flip()
    hod = 0
    gamezone = []
    gamezone_sprites = []
    while running:
        if koloda:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sprite.rect.collidepoint(event.pos):
                        gamezone.append(koloda[-1])
                        gamezone[-1].set_x(20 + 150 * len(gamezone))
                        gamezone[-1].set_y(250)
                        screen.blit(gamezone[-1].sprite.image, gamezone[-1].sprite.rect)
                        gamezone_sprites.append(gamezone[-1].sprite)
                        pygame.display.flip()
                        if check(gamezone):
                            pygame.time.wait(2000)
                            bita += gamezone
                            gamezone = []
                            hod = (hod + 1) % 2
                        elif type(gamezone[-1]) == Rom:
                            pass
                        elif type(gamezone[-1]) == Kompas:
                            pass
                        elif type(gamezone[-1]) == Yakor:
                            pass
                        elif type(gamezone[-1]) == Svecha:
                            pass
                        elif type(gamezone[-1]) == Shturval:
                            pass
                        elif type(gamezone[-1]) == Pistol:
                            pass
                        elif type(gamezone[-1]) == Mech:
                            pass
    pygame.quit()
