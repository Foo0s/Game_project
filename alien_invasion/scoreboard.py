import pygame.font


class Scoreboard():
    '''Класс для вывода игровой информации'''

    def __init__(self, a_g):
        '''Инициализирует атрибуты подсчета очков'''
        self.screen = a_g.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = a_g.settings
        self.stats = a_g.stats

        # Настройка шрифта для вывода счета
        self.text_color = (20, 10, 213)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения
        self.prep_score()

    def prep_score(self):
        '''Преобразует счет в графическое представление'''
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''Вывод счета на экран'''
        self.screen.blit(self.score_image, self.score_rect)
