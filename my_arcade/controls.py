import pygame

GAME_CONTROLS = {
    'DonkeyKong': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_SPACE: ('JUMP', 'Jump'),
            pygame.K_RETURN: ('FIRE', 'Start/Hammer')
        }
    },
    'KungFuMaster': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_UP: ('UP', 'Jump'),
            pygame.K_DOWN: ('DOWN', 'Crouch'),
            pygame.K_SPACE: ('FIRE', 'Punch/Kick'),
            pygame.K_a: ('LEFTFIRE', 'Left Attack'),
            pygame.K_d: ('RIGHTFIRE', 'Right Attack'),
            pygame.K_q: ('UPLEFTFIRE', 'Jump Left Attack'),
            pygame.K_e: ('UPRIGHTFIRE', 'Jump Right Attack'),
            pygame.K_z: ('DOWNLEFTFIRE', 'Crouch Left Attack'),
            pygame.K_c: ('DOWNRIGHTFIRE', 'Crouch Right Attack')
        }
    },
    'MarioBros': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_UP: ('UP', 'Move up'),
            pygame.K_DOWN: ('DOWN', 'Move down'),
            pygame.K_SPACE: ('FIRE', 'Jump'),
            pygame.K_q: ('UPLEFT', 'Jump diagonally left'),
            pygame.K_e: ('UPRIGHT', 'Jump diagonally right'),
            pygame.K_z: ('DOWNLEFT', 'Crouch and move left'),
            pygame.K_c: ('DOWNRIGHT', 'Crouch and move right'),
            pygame.K_w: ('UPFIRE', 'Jump and attack'),
            pygame.K_d: ('RIGHTFIRE', 'Attack right'),
            pygame.K_a: ('LEFTFIRE', 'Attack left'),
            pygame.K_s: ('DOWNFIRE', 'Crouch and attack')
        }
    },
    'Asteroids': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Rotate left'),
            pygame.K_RIGHT: ('RIGHT', 'Rotate right'),
            pygame.K_UP: ('UP', 'Thrust'),
            pygame.K_DOWN: ('DOWN', 'Reverse thrust'),
            pygame.K_SPACE: ('FIRE', 'Fire'),
            pygame.K_e: ('UPRIGHT', 'Thrust right'),
            pygame.K_q: ('UPLEFT', 'Thrust left'),
            pygame.K_w: ('UPFIRE', 'Thrust and fire'),
            pygame.K_d: ('RIGHTFIRE', 'Rotate right and fire'),
            pygame.K_a: ('LEFTFIRE', 'Rotate left and fire'),
            pygame.K_s: ('DOWNFIRE', 'Reverse thrust and fire'),
            pygame.K_r: ('UPRIGHTFIRE', 'Thrust right and fire'),
            pygame.K_f: ('UPLEFTFIRE', 'Thrust left and fire')
        }
    },
    'Pong': {
        'controls': {
            pygame.K_UP: ('RIGHT', 'Move paddle up'),
            pygame.K_DOWN: ('LEFT', 'Move paddle down'),
            pygame.K_SPACE: ('FIRE', 'Serve ball'),
            pygame.K_w: ('RIGHTFIRE', 'Move up and serve'),
            pygame.K_s: ('LEFTFIRE', 'Move down and serve')
        }
    },
    'Breakout': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move paddle left'),
            pygame.K_RIGHT: ('RIGHT', 'Move paddle right'),
            pygame.K_SPACE: ('FIRE', 'Launch ball')
        }
    },
    'BattleZone': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Rotate tank left'),
            pygame.K_RIGHT: ('RIGHT', 'Rotate tank right'),
            pygame.K_UP: ('UP', 'Move forward'),
            pygame.K_DOWN: ('DOWN', 'Move backward'),
            pygame.K_SPACE: ('FIRE', 'Fire cannon'),
            pygame.K_e: ('UPRIGHT', 'Move forward right'),
            pygame.K_q: ('UPLEFT', 'Move forward left'),
            pygame.K_c: ('DOWNRIGHT', 'Move backward right'),
            pygame.K_z: ('DOWNLEFT', 'Move backward left'),
            pygame.K_w: ('UPFIRE', 'Move forward and fire'),
            pygame.K_d: ('RIGHTFIRE', 'Rotate right and fire'),
            pygame.K_a: ('LEFTFIRE', 'Rotate left and fire'),
            pygame.K_s: ('DOWNFIRE', 'Move backward and fire')
        }
    },
    'Boxing': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_UP: ('UP', 'Move up'),
            pygame.K_DOWN: ('DOWN', 'Move down'),
            pygame.K_SPACE: ('FIRE', 'Punch'),
            pygame.K_e: ('UPRIGHT', 'Move up-right'),
            pygame.K_q: ('UPLEFT', 'Move up-left'),
            pygame.K_c: ('DOWNRIGHT', 'Move down-right'),
            pygame.K_z: ('DOWNLEFT', 'Move down-left'),
            pygame.K_w: ('UPFIRE', 'Move up and punch'),
            pygame.K_d: ('RIGHTFIRE', 'Move right and punch'),
            pygame.K_a: ('LEFTFIRE', 'Move left and punch'),
            pygame.K_s: ('DOWNFIRE', 'Move down and punch')
        }
    },
    'DemonAttack': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_SPACE: ('FIRE', 'Fire laser'),
            pygame.K_a: ('LEFTFIRE', 'Move left and fire'),
            pygame.K_d: ('RIGHTFIRE', 'Move right and fire')
        }
    },
    'DoubleDunk': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Move left'),
            pygame.K_RIGHT: ('RIGHT', 'Move right'),
            pygame.K_UP: ('UP', 'Move up'),
            pygame.K_DOWN: ('DOWN', 'Move down'),
            pygame.K_SPACE: ('FIRE', 'Shoot/Select play'),
            pygame.K_e: ('UPRIGHT', 'Move up-right'),
            pygame.K_q: ('UPLEFT', 'Move up-left'),
            pygame.K_c: ('DOWNRIGHT', 'Move down-right'),
            pygame.K_z: ('DOWNLEFT', 'Move down-left'),
            pygame.K_w: ('UPFIRE', 'Move up and shoot'),
            pygame.K_d: ('RIGHTFIRE', 'Move right and shoot'),
            pygame.K_a: ('LEFTFIRE', 'Move left and shoot'),
            pygame.K_s: ('DOWNFIRE', 'Move down and shoot')
        }
    },
    'Enduro': {
        'controls': {
            pygame.K_LEFT: ('LEFT', 'Steer left'),
            pygame.K_RIGHT: ('RIGHT', 'Steer right'),
            pygame.K_DOWN: ('DOWN', 'Brake'),
            pygame.K_SPACE: ('FIRE', 'Accelerate'),
            pygame.K_c: ('DOWNRIGHT', 'Brake and steer right'),
            pygame.K_z: ('DOWNLEFT', 'Brake and steer left'),
            pygame.K_d: ('RIGHTFIRE', 'Accelerate and steer right'),
            pygame.K_a: ('LEFTFIRE', 'Accelerate and steer left')
        }
    }
}
