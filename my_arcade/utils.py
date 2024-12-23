import numpy as np
import pygame
import os

def display_arr(screen, arr, video_size, transpose):
    """Simple display function with fixed scaling"""
    if transpose:
        arr = arr.swapaxes(0, 1)
    surf = pygame.surfarray.make_surface(arr)
    pygame.transform.scale(surf, video_size, screen)

def get_action_number(game_name, action_name):
    """Map action names to ALE action numbers for each game"""
    action_maps = {
        'SpaceInvaders': {
            'NOOP': 0, 'FIRE': 1, 'RIGHT': 2, 'LEFT': 3,
            'RIGHTFIRE': 4, 'LEFTFIRE': 5
        },
        'Breakout': {
            'NOOP': 0,
            'FIRE': 1,    # Launch ball
            'RIGHT': 2,   # Move paddle right
            'LEFT': 3,    # Move paddle left
            'START': 1    # Start game (same as FIRE)
        },
        'Pong': {
            'NOOP': 0, 'FIRE': 1, 'RIGHT': 2, 'LEFT': 3,
            'RIGHTFIRE': 4, 'LEFTFIRE': 5, 'UP': 2, 'DOWN': 3
        },
        'Asteroids': {
            'NOOP': 0, 'FIRE': 1, 'RIGHT': 2, 'LEFT': 3,
            'UP': 4, 'DOWN': 5, 'HYPERSPACE': 6,
            'RIGHTFIRE': 7, 'LEFTFIRE': 8
        },
        'BattleZone': {
            'NOOP': 0, 'FIRE': 1, 'RIGHT': 2, 'LEFT': 3,
            'UP': 4, 'DOWN': 5
        },
        'Pacman': {
            'NOOP': 0, 'UP': 1, 'RIGHT': 2, 'LEFT': 3, 'DOWN': 4
        },
        'DonkeyKong': {
            'NOOP': 0, 'UP': 1, 'RIGHT': 2, 'LEFT': 3,
            'DOWN': 4, 'JUMP': 5, 'START': 6
        },
        'MarioBros': {
            'NOOP': 0, 'UP': 1, 'RIGHT': 2, 'LEFT': 3,
            'DOWN': 4, 'JUMP': 5, 'START': 6
        },
        'KungFuMaster': {
            'NOOP': 0,    # No operation
            'UP': 1,      # Jump
            'RIGHT': 2,   # Move right
            'LEFT': 3,    # Move left
            'DOWN': 4,    # Crouch
            'PUNCH': 12,  # Changed from FIRE to PUNCH
            'KICK': 13    # Kick
        }
    }
    return action_maps.get(game_name, {}).get(action_name, 0)