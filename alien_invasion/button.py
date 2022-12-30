'''Создание кнопок'''
import pygame.font


class Button():
    def __init__(self, ai_gm, msg):
        '''Инициализирует атрибуты кнопки.'''
        self.screen = ai_gm.screen
        self.screen_rect = self.screen.get_rect()

        # Св-ва кнопки.
        self.width, self.height = 120, 105
        self.button_color = (0, 160, 189)
        self.text_color = (233, 233, 1)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Передача сообщения - 1 раз.
        self.us_message(msg)

    def us_message(self, mess):
        '''Выравнивание текста по прямоугольнику, размещение.'''
        self.mess_image = self.font.render(mess, True, self.text_color, self.button_color)
        self.mess_image_rect = self.mess_image.get_rect()
        self.mess_image_rect.center = self.rect.center

    def draw_button(self):
        '''Отображает кнопку на экране'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.mess_image, self.mess_image_rect)
