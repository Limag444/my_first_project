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
        self.sprite.image = pygame.transform.scale(load_image('пистоль\\пистоль' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Popugai(Karta):
    def __init__(self, points):
        super(Popugai, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('попугай\\попугай' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Mech(Karta):
    def __init__(self, points):
        super(Mech, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('меч\\меч' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Sunduk(Karta):
    def __init__(self, points):
        super(Sunduk, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('сундук\\сундук' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Kluch(Karta):
    def __init__(self, points):
        super(Kluch, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('ключ\\ключ' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Svecha(Karta):
    def __init__(self, points):
        super(Svecha, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('свеча\\свеча' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Shturval(Karta):
    def __init__(self, points):
        super(Shturval, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('штурвал\\штурвал' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Kompas(Karta):
    def __init__(self, points):
        super(Kompas, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('компас\\компас' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Yakor(Karta):
    def __init__(self, points):
        super(Yakor, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('якорь\\якорь' + str(points) + '.png'), (100, 150))
        self.sprite.rect = self.sprite.image.get_rect()

    def set_x(self, x):
        self.sprite.rect.x = x

    def set_y(self, y):
        self.sprite.rect.y = y


class Rom(Karta):
    def __init__(self, points):
        super(Rom, self).__init__(points)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(load_image('ром\\ром' + str(points) + '.png'), (100, 150))
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


def get_cards(gamezone, player):
    for i in gamezone:
        if type(i) == Kompas:
            player['компас'].append(i)
        if type(i) == Rom:
            player['ром'].append(i)
        if type(i) == Yakor:
            player['якорь'].append(i)
        if type(i) == Svecha:
            player['свеча'].append(i)
        if type(i) == Shturval:
            player['штурвал'].append(i)
        if type(i) == Sunduk:
            player['сундук'].append(i)
        if type(i) == Kluch:
            player['ключ'].append(i)
        if type(i) == Mech:
            player['меч'].append(i)
        if type(i) == Pistol:
            player['пистоль'].append(i)
        if type(i) == Popugai:
            player['попугай'].append(i)


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
first_player = {'ром': [], 'компас': [], 'якорь': [], 'пистоль': [], 'попугай': [], 'свеча': [], 'штурвал': [],
                'ключ': [], 'сундук': [], 'меч': []}
second_player = {'ром': [], 'компас': [], 'якорь': [], 'пистоль': [], 'попугай': [], 'свеча': [], 'штурвал': [],
                 'ключ': [], 'сундук': [], 'меч': []}
if __name__ == '__main__':
    size = width, height = 0, 0
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Остров сокровищ')
    sprite2 = pygame.sprite.Sprite()
    all_sprites = pygame.sprite.Group()
    zastavka = load_image('заставка.png')
    tzastavka = pygame.transform.scale(zastavka, (1375, 775))
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
    first_player_rect = pygame.rect.Rect(0, 600, 675, 200)
    second_player_rect = pygame.rect.Rect(695, 600, 685, 200)
    razd = pygame.rect.Rect(675, 600, 20, 200)
    pygame.draw.rect(screen, pygame.Color('black'), razd)
    pygame.draw.rect(screen, pygame.Color('brown'), second_player_rect)
    pygame.draw.rect(screen, pygame.Color('brown'), first_player_rect)
    running = True
    pygame.display.flip()
    hod = 0
    gamezone = []
    gamezone_sprites = pygame.sprite.Group()
    first_player_sprites = pygame.sprite.Group()
    while running:
        if koloda:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sprite.rect.collidepoint(event.pos):
                        gamezone.append(koloda.pop())
                        gamezone[-1].set_x(70 + 110 * len(gamezone))
                        gamezone[-1].set_y(280)
                        gamezone_sprites.add(gamezone[-1].sprite)
                        gamezone_sprites.draw(screen)
                        pygame.display.flip()
                        if check(gamezone):
                            pygame.time.wait(2000)
                            bita += gamezone
                            gamezone = []
                            for i in gamezone_sprites.sprites():
                                gamezone_sprites.remove(i)
                            hod = (hod + 1) % 2
                            screen.fill(pygame.Color('yellow'))
                            all_sprites.draw(screen)
                            pygame.draw.rect(screen, pygame.Color('black'), razd)
                            pygame.draw.rect(screen, pygame.Color('brown'), second_player_rect)
                            pygame.draw.rect(screen, pygame.Color('brown'), first_player_rect)
                            pygame.display.flip()
                        elif type(gamezone[-1]) == Rom:
                            pygame.time.wait(2000)
                            if len(koloda) >= 1:
                                gamezone.append(koloda.pop())
                                gamezone[-1].set_x(70 + 110 * len(gamezone))
                                gamezone[-1].set_y(280)
                                gamezone_sprites.add(gamezone[-1].sprite)
                                if len(koloda) >= 1:
                                    gamezone.append(koloda.pop())
                                    gamezone[-1].set_x(70 + 110 * len(gamezone))
                                    gamezone[-1].set_y(280)
                                    gamezone_sprites.add(gamezone[-1].sprite)
                            gamezone_sprites.draw(screen)
                            pygame.display.flip()
                            if check(gamezone):
                                pygame.time.wait(2000)
                                bita += gamezone
                                gamezone = []
                                for i in gamezone_sprites.sprites():
                                    gamezone_sprites.remove(i)
                                hod = (hod + 1) % 2
                                screen.fill(pygame.Color('yellow'))
                                all_sprites.draw(screen)
                                pygame.draw.rect(screen, pygame.Color('black'), razd)
                                pygame.draw.rect(screen, pygame.Color('brown'), second_player_rect)
                                pygame.draw.rect(screen, pygame.Color('brown'), first_player_rect)
                                pygame.display.flip()
                        elif type(gamezone[-1]) == Kompas:
                            pass
                        elif type(gamezone[-1]) == Svecha:
                            pass
                        elif type(gamezone[-1]) == Shturval:
                            pass
                        elif type(gamezone[-1]) == Pistol:
                            pass
                        elif type(gamezone[-1]) == Mech:
                            pass
                    if first_player_rect.collidepoint(event.pos) and hod == 0:
                        hod = (hod + 1) % 2
                        for i in gamezone_sprites.sprites():
                            gamezone_sprites.remove(i)
                        for i in first_player_sprites.sprites():
                            first_player_sprites.remove(i)
                        screen.fill(pygame.Color('yellow'))
                        all_sprites.draw(screen)
                        pygame.draw.rect(screen, pygame.Color('black'), razd)
                        pygame.draw.rect(screen, pygame.Color('brown'), second_player_rect)
                        pygame.draw.rect(screen, pygame.Color('brown'), first_player_rect)
                        get_cards(gamezone, first_player)
                        print(first_player)
                        for tip in range(len(first_player.keys())):
                            for i in range(len(first_player[list(first_player.keys())[tip]])):
                                print('hello')
                                a = sorted(first_player[list(first_player.keys())[tip]], key=lambda x: x.get_points())
                                a[i].sprite.x = 20 + 50 * tip
                                a[i].sprite.y = 700 + 10 * i
                                first_player_sprites.add(a[i].sprite)
                        first_player_sprites.draw(screen)
                        gamezone = []
                        pygame.display.flip()
                    pygame.display.flip()
pygame.quit()
