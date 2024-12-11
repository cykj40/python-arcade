from gymnasium.envs.registration import register

# Register custom wrapped versions of Atari games if needed
games = [
    'SpaceInvaders',
    'Pong',
    'Breakout',
    'Asteroids',
    'MsPacman',
    'BattleZone',
    'Boxing',
    'DemonAttack',
    'DoubleDunk',
    'Enduro',
    'DonkeyKong',
    'KungFuMaster',
    'MarioBros'
]

for game in games:
    register(
        id=f'CustomAtari{game}-v0',
        entry_point=f'my_arcade.envs.atari_env:Custom{game}Env',
    )

