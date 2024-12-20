import os
from turtle import Terminator
import gymnasium as gym
import ale_py
import pygame
from my_arcade.controls import GAME_CONTROLS
from my_arcade.sound import SoundManager
from my_arcade.render_utils import display_arr
from my_arcade.utils import get_action_number

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_ale():
    try:
        # Register ALE environments with gymnasium
        gym.register_envs(ale_py)
        return True
    except Exception as e:
        print(f"Error initializing ALE: {e}")
        print("\nPlease ensure you have installed the required packages:")
        print("pip install ale-py")
        print("pip install gymnasium[atari]")
        print("pip install 'gymnasium[accept-rom-license]'")
        return False

def get_available_games():
    games = {}
    game_list = [
        'SpaceInvaders', 'Breakout', 'Pong', 'DonkeyKong', 'MarioBros',
        'KungFuMaster', 'Boxing', 'BattleZone', 'Asteroids', 'DemonAttack',
        'Enduro', 'DoubleDunk', 'Pacman', 'MsPacman', 'Phoenix', 'Qbert',
        'RiverRaid', 'Seaquest', 'Tennis', 'VideoPinball'
    ]
    for i, game in enumerate(game_list):
        games[str(i + 1)] = {
            'id': f'ALE/{game}-v5',
            'name': game
        }
    return games

def display_menu(games):
    print("\nPython Arcade Menu")
    print("=================")
    for key, game in games.items():
        print(f"{key}. {game['name']}")
    print("\nQ. Quit")
    return input("\nSelect a game (1-13, Q to quit): ").upper()

def play_game(game_id, game_name):
    try:
        pygame.init()
        sound_manager = SoundManager()
        
        # Print available actions before game starts
        temp_env = gym.make(game_id)
        print(f"\nAvailable actions for {game_name}:")
        print(temp_env.unwrapped.get_action_meanings())
        temp_env.close()
        
        # Create game environment
        env = gym.make(
            game_id,
            render_mode="rgb_array",
            frameskip=1,
            repeat_action_probability=0.0,
            full_action_space=False  # Changed to False for basic controls
        )
        
        obs, _ = env.reset()
        rendered = env.render()
        
        # Set up display with fixed scaling
        scale = 3  # Fixed scale factor
        video_size = (rendered.shape[1] * scale, rendered.shape[0] * scale)
        screen = pygame.display.set_mode(video_size)
        pygame.display.set_caption(f"Playing {game_name}")
        
        # Show controls
        controls = GAME_CONTROLS.get(game_name, {}).get('controls', {})
        print("\nGame Controls:")
        for key, (action_name, desc) in controls.items():
            action_num = get_action_number(game_name, action_name)
            print(f"{pygame.key.name(key)}: {desc} (Action: {action_num})")
        
        clock = pygame.time.Clock()
        running = True
        
        while running:
            clock.tick(60)
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
            
            # Get pressed keys and map to action
            keys = pygame.key.get_pressed()
            action = 0  # NOOP default
            
            # Check controls and update action
            for key, (action_name, _) in controls.items():
                if keys[key]:
                    new_action = get_action_number(game_name, action_name)
                    if new_action > 0:  # Only update if it's not NOOP
                        action = new_action
                        break
            
            # Execute action
            obs, reward, terminated, truncated, info = env.step(action)
            
            # Render game
            rendered = env.render()
            surf = pygame.surfarray.make_surface(rendered.swapaxes(0, 1))
            pygame.transform.scale(surf, video_size, screen)
            pygame.display.flip()
            
            if terminated or truncated:
                print(f"\nGame Over! Score: {info.get('score', 0)}")
                pygame.time.wait(2000)
                break
        
        env.close()
        pygame.quit()
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nPlease ensure you have installed all required packages:")
        print("pip install ale-py gymnasium[atari] 'gymnasium[accept-rom-license]' pygame")

def main():
    if not initialize_ale():
        input("\nPress Enter to exit...")
        return

    while True:
        clear_screen()
        games = get_available_games()
        choice = display_menu(games)
        
        if choice == 'Q':
            print("\nThanks for playing!")
            break
        elif choice in games:
            game = games[choice]
            play_game(game['id'], game['name'])
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
