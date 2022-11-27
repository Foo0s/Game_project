import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Класс, который создает 1 пришельца.'''

    def __init__(self, ai_game):
        '''Инициализирует пришельца и назначение атрибута rect.'''
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load("images/pngwing.com (2).png")
        self.image = pygame.transform.scale(self.image, (87, 50))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)