DefenseMode = 0
AttackMode = 1

class Ship:
    def __init__(self, mode=AttackMode):
        self.mode = mode

    # Switches the state of this ship to Attack mode.
    def switch_attack_mode(self):
        self.mode = AttackMode
        # TODO

    # Switches the state of this ship to Defense mode.
    def switch_defense_mode(self):
        self.mode = DefenseMode
        # TODO

    # Returns whether this ship is currently in Attack mode or not.
    def in_attack_mode(self):
        return self.mode == AttackMode

    # Returns whether this ship is currently in Defense mode or not.
    def in_defense_mode(self):
        return self.mode == DefenseMode

    # Updates the state of this ship per frame.
    def update(self):
        pass

    # Draws this ship onto the given surface.
    def draw(self, surface):
        pass