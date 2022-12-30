class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion'''

    def __init__(self):
        '''Инициализирует настройки игры.'''
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 200, 30)
        self.name_game = "Alien Invasion"
        self.alien_speed = 4.2
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1

        # Настройка корабля
        self.ship_speed = 4.2
        self.ship_limit = 3

        # Св-ва и настройки снарядов
        self.bullet_speed = 1.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (10, 32, 198)

        # Макс кол-во снарядов
        self.bullet_allowed = 4
