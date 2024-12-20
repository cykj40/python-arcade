from gymnasium.envs.registration import register

# Only include games with good human controls
games = [
    'SpaceInvaders',    # Classic shooter
    'Breakout',         # Paddle game
    'Pong',            # Paddle game
    'DonkeyKong',      # Platform
    'MarioBros',       # Platform
    'KungFuMaster',    # Fighting
    'Boxing',          # Fighting
    'BattleZone',      # 3D Tank
    'Asteroids',       # Space shooter
    'DemonAttack',     # Space shooter
    'Enduro',          # Racing
    'DoubleDunk',      # Sports
    'Pacman',          # Maze
    'MsPacman',        # Maze
    'Phoenix',         # Space shooter
    'Qbert',           # Platform
    'RiverRaid',       # Shooter
    'Seaquest',        # Underwater
    'Tennis',          # Sports
    'VideoPinball'     # Pinball
]

for game in games:
    register(
        id=f'CustomAtari{game}-v0',
        entry_point=f'my_arcade.envs.atari_env:Custom{game}Env',
    )

