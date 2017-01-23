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

            if x >= 17 and y >= 595 and x <= 17 + 91 and y <= 75 + 595:
                sound.Plopperdeplop.tune(self, 'click')
                from screens.main_menu import MainScreen
                self.game.set_screen(MainScreen(self.game))
            elif x >= 106 and y >= 226 and x <= 400 and y <= 310:
                sound.Plopperdeplop.tune(self, 'click')
                from screens.pregame.pregame_introduction import PreGameIntroductionScreen
                self.game.set_screen(PreGameIntroductionScreen(self.game))
            elif x >= 623 and y >= 221 and x <= 923 and y <= 305:
                sound.Plopperdeplop.tune(self, 'click')
                from screens.pregame.pregame_rules import RulesScreen
                self.game.set_screen(RulesScreen(self.game, self))
            elif x >= 726 and y >= 586 and x <= 994 and y <= 670:
                sound.Plopperdeplop.tune(self, 'click')
                self.game.set_screen(screens.game.session.SessionScreen(self.game))

    # Draws the components of this 'pregame instructions' screen.
    def draw(self):
        self.game.surface.blit(self.image, (0, 0))