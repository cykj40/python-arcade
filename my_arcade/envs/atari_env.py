import gymnasium as gym
from gymnasium import Wrapper
import numpy as np

class BaseAtariEnv(Wrapper):
    def __init__(self, game_id):
        env = gym.make(
            game_id, 
            render_mode="rgb_array",
            frameskip=1,
            repeat_action_probability=0.0,
            full_action_space=True
        )
        self.frames = []
        super().__init__(env)
    
    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        # Keep last 2 frames for flickering prevention
        self.frames.append(obs)
        if len(self.frames) > 2:
            self.frames.pop(0)
        # Return max of last 2 frames
        max_frame = np.maximum(self.frames[-1], self.frames[-2] if len(self.frames) > 1 else self.frames[-1])
        return max_frame, reward, terminated, truncated, info

# Create custom env classes for each game
class CustomSpaceInvadersEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/SpaceInvaders-v5")

class CustomBreakoutEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Breakout-v5")

class CustomDonkeyKongEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/DonkeyKong-v5")

class CustomKungFuMasterEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/KungFuMaster-v5")

class CustomMarioBrosEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/MarioBros-v5")

class CustomPongEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Pong-v5")

class CustomPacmanEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Pacman-v5")

class CustomMsPacmanEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/MsPacman-v5")

class CustomPhoenixEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Phoenix-v5")

class CustomQbertEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Qbert-v5")

class CustomRiverRaidEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/RiverRaid-v5")

class CustomSeaquestEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Seaquest-v5")

class CustomTennisEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/Tennis-v5")

class CustomVideoPinballEnv(BaseAtariEnv):
    def __init__(self):
        super().__init__("ALE/VideoPinball-v5")
