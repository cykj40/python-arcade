import gymnasium as gym
from gymnasium import Wrapper
import numpy as np

class BaseAtariEnv(Wrapper):
    def __init__(self, game_id):
        env = gym.make(
            game_id, 
            render_mode="rgb_array",
            frameskip=2,
            repeat_action_probability=0.0,
            full_action_space=True,
            obs_type="rgb"
        )
        self.frame_buffer = []
        self.buffer_size = 1
        super().__init__(env)
    
    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        # Maintain frame buffer for smoother rendering
        self.frame_buffer.append(obs)
        if len(self.frame_buffer) > self.buffer_size:
            self.frame_buffer.pop(0)
        # Return average of buffered frames for smoother visuals
        smooth_frame = np.mean(self.frame_buffer, axis=0).astype(np.uint8)
        return smooth_frame, reward, terminated, truncated, info

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
