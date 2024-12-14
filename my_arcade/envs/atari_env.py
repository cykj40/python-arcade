import gymnasium as gym
from gymnasium import Wrapper

class BaseAtariEnv(Wrapper):
    def __init__(self, game_id):
        env = gym.make(game_id, render_mode="human")
        super().__init__(env)

# Create custom env classes for each game
class CustomSpaceInvadersEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/SpaceInvaders-v5")

class CustomPongEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Pong-v5")

class CustomBreakoutEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Breakout-v5")

class CustomAsteroidsEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Asteroids-v5")

class CustomMsPacmanEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/MsPacman-v5")

class CustomBattleZoneEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/BattleZone-v5")

class CustomBoxingEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Boxing-v5")

class CustomDemonAttackEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/DemonAttack-v5")

class CustomDoubleDunkEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/DoubleDunk-v5")

class CustomEnduroEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Enduro-v5")

class CustomDonkeyKongEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/DonkeyKong-v5")

class CustomKungFuMasterEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/KungFuMaster-v5")

class CustomMarioBrosEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/MarioBros-v5")
