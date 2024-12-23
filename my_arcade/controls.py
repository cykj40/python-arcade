import pygame

GAME_CONTROLS = {
    'SpaceInvaders': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_SPACE: ('FIRE', 'Fire')
        }
    },
    'Breakout': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move paddle left'),
            pygame.K_RIGHT: ('RIGHT', 'Move paddle right'),
            pygame.K_SPACE: ('FIRE', 'Launch ball'),
            pygame.K_RETURN: ('START', 'Start game')
        }
    },
    'Pong': {
        'controls': {
            pygame.K_UP: ('UP', 'Move paddle up'),
            pygame.K_DOWN: ('DOWN', 'Move paddle down'),
            pygame.K_RETURN: ('FIRE', 'Start game/Serve')
        }
    },
    'Asteroids': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Rotate left'),
            pygame.K_RIGHT: ('RIGHT', 'Rotate right'),
            pygame.K_UP: ('UP', 'Thrust'),
            pygame.K_SPACE: ('FIRE', 'Fire'),
            pygame.K_LSHIFT: ('HYPERSPACE', 'Hyperspace')
        }
    },
    'BattleZone': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Rotate tank left'),
            pygame.K_RIGHT: ('RIGHT', 'Rotate tank right'),
            pygame.K_UP: ('UP', 'Move forward'),
            pygame.K_DOWN: ('DOWN', 'Move backward'),
            pygame.K_SPACE: ('FIRE', 'Fire')
        }
    },
    'Pacman': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_UP: ('UP', 'Move up'),
            pygame.K_DOWN: ('DOWN', 'Move down')
        }
    },
    'DonkeyKong': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_SPACE: ('JUMP', 'Jump'),
            pygame.K_RETURN: ('START', 'Start game')
        }
    },
    'MarioBros': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_SPACE: ('JUMP', 'Jump'),
            pygame.K_RETURN: ('START', 'Start game')
        }
    },
    'KungFuMaster': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_UP: ('UP', 'Jump'),
            pygame.K_DOWN: ('DOWN', 'Crouch'),
            pygame.K_x: ('PUNCH', 'Punch'),
            pygame.K_z: ('KICK', 'Kick')
        }
    },
    'DemonAttack': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_SPACE: ('FIRE', 'Fire laser')
        }
    },
    'Enduro': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Steer left'),
            pygame.K_RIGHT: ('RIGHT', 'Steer right'),
            pygame.K_SPACE: ('UP', 'Accelerate'),
            pygame.K_DOWN: ('DOWN', 'Brake')
        }
    },
    'DoubleDunk': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_SPACE: ('FIRE', 'Shoot/Pass'),
            pygame.K_UP: ('UP', 'Move up'),
            pygame.K_DOWN: ('DOWN', 'Move down')
        }
    }
}
