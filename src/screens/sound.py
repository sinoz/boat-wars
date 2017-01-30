import pygame
current_song = ''

class Plopperdeplop:
    def tune(self, sound):
        if sound == 'click':
            Snd = pygame.mixer.Sound('resources/mp3/Click.ogg')
        elif sound == 'cannon_big':
            Snd = pygame.mixer.Sound('resources/mp3/Cannon_big_ship.ogg')
        elif sound == 'cannon_small':
            Snd = pygame.mixer.Sound('resources/mp3/Cannon_small_ship.ogg')
        elif sound == 'explosion_ship':
            Snd = pygame.mixer.Sound('resources/mp3/Explosion_ship.ogg')
        elif sound == 'movement':
            Snd = pygame.mixer.Sound('resources/mp3/Movement.ogg')
        elif sound == 'card_flip' :
            Snd = pygame.mixer.Sound('resources/mp3/Card.ogg')
        elif sound ==  'change_mode':
            Snd = pygame.mixer.Sound('resources/mp3/Change_mode.ogg')

        pygame.mixer.Sound.play(Snd)
        Snd.set_volume(0.3)

    def music(self, song):
        if song == 'intro':
            pygame.mixer.music.load('resources/mp3/intro.mp3')
        elif song == 'credits':
            pygame.mixer.music.load('resources/mp3/Credits.mp3')
        elif song == 'high_scores':
            pygame.mixer.music.load('resources/mp3/High_scores.mp3')
        elif song == 'victory':
            pygame.mixer.music.load('resources/mp3/Victory.mp3')
        elif song == 'battle_music':
            pygame.mixer.music.load('resources/mp3/Battle_music.mp3')

        pygame.mixer.music.play(-1)
        global current_song
        current_song = song
        pygame.mixer.music.set_volume(self.canvas.volume)