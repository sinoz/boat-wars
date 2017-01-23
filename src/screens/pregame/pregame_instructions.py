import pygame
import screens.sound as sound
import screens.game.session

class PreGameInstructionsScreen:
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('resources/screens/' + game.language + '/pregame/pregame_instructions.jpg')

    # Updates this 'pregame instructions' screen.
    def update(self):
        pass

    # Handles an event.
    def on_event(self, event): # TODO use widget.button instead of hardcoding
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cursor = pygame.mouse.get_cursor()
            mouse_pos = pygame.mouse.get_pos()

            x = mouse_pos[0]
            y = mouse_pos[1]

            print(x, y)

            if x >= 175 and y >= 526 and x <= 452 and y <= 611:
                sound.Plopperdeplop.tune(self, 'click')
                from screens.main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))
            elif x >= 106 and y >= 225 and x <= 402 and y <= 306:
                sound.Plopperdeplop.tune(self, 'click')
                from screens.pregame.pregame_introduction import PreGameIntroductionScreen
                self.game.set_screen(PreGameIntroductionScreen(self.game))
            elif x >= 623 and y >= 219 and x <= 925 and y <= 303:
                sound.Plopperdeplop.tune(self, 'click')
                from screens.pregame.pregame_rules import RulesScreen
                self.game.set_screen(RulesScreen(self.game))
            elif x >= 593 and y >= 523 and x <= 887 and y <= 604:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.game.session.SessionScreen(self.game))

    # Draws the components of this 'pregame instructions' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))