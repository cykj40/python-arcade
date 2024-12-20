import pygame
import numpy as np

def display_arr(screen, arr, video_size, transpose):
    """Displays a numpy array on screen with proper scaling."""
    arr_min, arr_max = np.min(arr), np.max(arr)
    arr = 255.0 * (arr - arr_min) / (arr_max - arr_min)
    pyg_img = pygame.surfarray.make_surface(arr.swapaxes(0, 1) if transpose else arr)
    pyg_img = pygame.transform.scale(pyg_img, video_size)
    screen.blit(pyg_img, (0, 0)) 