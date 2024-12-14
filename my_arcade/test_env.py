import os
import gymnasium as gym
import ale_py
import pygame
from my_arcade.controls import GAME_CONTROLS
from my_arcade.sound import SoundManager

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
    for i, game in enumerate(['SpaceInvaders', 'Pong', 'Breakout', 'Asteroids', 
                            'Pacman', 'BattleZone', 'Boxing', 'DemonAttack', 
                            'DoubleDunk', 'Enduro', 'DonkeyKong', 'KungFuMaster', 'MarioBros']):
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
        sound_manager.load_game_sounds(game_name)
        
        # Create environment with human rendering and frameskip=1 for better control
        env = gym.make(game_id, render_mode="human", frameskip=1)
        observation, info = env.reset()
        
        # Get game-specific controls
        game_controls = GAME_CONTROLS.get(game_name, {}).get('controls', {})
        
        print(f"\nPlaying {game_name}")
        print("Controls:")
        for key, (action, desc) in game_controls.items():
            print(f"{pygame.key.name(key)}: {desc}")
        print("ESC: Return to menu")
        
        clock = pygame.time.Clock()
        running = True
        
        while running:
            clock.tick(60)  # 60 FPS
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            
            # Default to NOOP
            action = 0  # NOOP
            
            # Map keyboard input to ALE actions based on game
            if game_name == 'SpaceInvaders':
                if keys[pygame.K_LEFT]:
                    action = 3  # LEFT
                elif keys[pygame.K_RIGHT]:
                    action = 2  # RIGHT
                
                # Handle fire combinations
                if keys[pygame.K_SPACE]:
                    if keys[pygame.K_LEFT]:
                        action = 5  # LEFTFIRE
                    elif keys[pygame.K_RIGHT]:
                        action = 4  # RIGHTFIRE
                    else:
                        action = 1  # FIRE
            elif game_name == 'KungFuMaster':
                # Basic movements
                if keys[pygame.K_UP]:
                    action = 1  # UP
                elif keys[pygame.K_RIGHT]:
                    action = 2  # RIGHT
                elif keys[pygame.K_LEFT]:
                    action = 3  # LEFT
                elif keys[pygame.K_DOWN]:
                    action = 4  # DOWN
                
                # Diagonal movements
                if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                    action = 5  # DOWNRIGHT
                elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                    action = 6  # DOWNLEFT
                
                # Attack moves
                if keys[pygame.K_d]:
                    action = 7  # RIGHTFIRE
                elif keys[pygame.K_a]:
                    action = 8  # LEFTFIRE
                elif keys[pygame.K_DOWN] and keys[pygame.K_SPACE]:
                    action = 9  # DOWNFIRE
                elif keys[pygame.K_e]:
                    action = 10  # UPRIGHTFIRE
                elif keys[pygame.K_q]:
                    action = 11  # UPLEFTFIRE
                elif keys[pygame.K_c]:
                    action = 12  # DOWNRIGHTFIRE
                elif keys[pygame.K_z]:
                    action = 13  # DOWNLEFTFIRE
                elif keys[pygame.K_SPACE]:
                    action = 7  # Default attack (RIGHTFIRE)
            elif game_name == 'Asteroids':
                # Basic movements
                if keys[pygame.K_UP]:
                    action = 2  # UP (Thrust)
                elif keys[pygame.K_RIGHT]:
                    action = 3  # RIGHT (Rotate right)
                elif keys[pygame.K_LEFT]:
                    action = 4  # LEFT (Rotate left)
                elif keys[pygame.K_DOWN]:
                    action = 5  # DOWN (Reverse thrust)
                
                # Diagonal movements
                if keys[pygame.K_e]:
                    action = 6  # UPRIGHT
                elif keys[pygame.K_q]:
                    action = 7  # UPLEFT
                
                # Fire combinations
                if keys[pygame.K_w]:
                    action = 8  # UPFIRE
                elif keys[pygame.K_d]:
                    action = 9  # RIGHTFIRE
                elif keys[pygame.K_a]:
                    action = 10  # LEFTFIRE
                elif keys[pygame.K_s]:
                    action = 11  # DOWNFIRE
                elif keys[pygame.K_r]:
                    action = 12  # UPRIGHTFIRE
                elif keys[pygame.K_f]:
                    action = 13  # UPLEFTFIRE
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE
            elif game_name == 'Pong':
                # Basic movements
                if keys[pygame.K_UP]:
                    action = 2  # RIGHT (Move Up)
                elif keys[pygame.K_DOWN]:
                    action = 3  # LEFT (Move Down)
                
                # Serve combinations
                if keys[pygame.K_w]:
                    action = 4  # RIGHTFIRE (Move up and serve)
                elif keys[pygame.K_s]:
                    action = 5  # LEFTFIRE (Move down and serve)
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE (Serve)
            elif game_name == 'Breakout':
                # Basic movements
                if keys[pygame.K_LEFT]:
                    action = 3  # LEFT
                elif keys[pygame.K_RIGHT]:
                    action = 2  # RIGHT
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE (Launch ball)
            elif game_name == 'BattleZone':
                # Basic movements
                if keys[pygame.K_UP]:
                    action = 2  # UP (Forward)
                elif keys[pygame.K_RIGHT]:
                    action = 3  # RIGHT
                elif keys[pygame.K_LEFT]:
                    action = 4  # LEFT
                elif keys[pygame.K_DOWN]:
                    action = 5  # DOWN (Backward)
                
                # Diagonal movements
                if keys[pygame.K_e]:
                    action = 6  # UPRIGHT
                elif keys[pygame.K_q]:
                    action = 7  # UPLEFT
                elif keys[pygame.K_c]:
                    action = 8  # DOWNRIGHT
                elif keys[pygame.K_z]:
                    action = 9  # DOWNLEFT
                
                # Fire combinations
                if keys[pygame.K_w]:
                    action = 10  # UPFIRE
                elif keys[pygame.K_d]:
                    action = 11  # RIGHTFIRE
                elif keys[pygame.K_a]:
                    action = 12  # LEFTFIRE
                elif keys[pygame.K_s]:
                    action = 13  # DOWNFIRE
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE
            elif game_name == 'Boxing':
                # Basic movements
                if keys[pygame.K_UP]:
                    action = 2  # UP
                elif keys[pygame.K_RIGHT]:
                    action = 3  # RIGHT
                elif keys[pygame.K_LEFT]:
                    action = 4  # LEFT
                elif keys[pygame.K_DOWN]:
                    action = 5  # DOWN
                
                # Diagonal movements
                if keys[pygame.K_e]:
                    action = 6  # UPRIGHT
                elif keys[pygame.K_q]:
                    action = 7  # UPLEFT
                elif keys[pygame.K_c]:
                    action = 8  # DOWNRIGHT
                elif keys[pygame.K_z]:
                    action = 9  # DOWNLEFT
                
                # Punch combinations
                if keys[pygame.K_w]:
                    action = 10  # UPFIRE
                elif keys[pygame.K_d]:
                    action = 11  # RIGHTFIRE
                elif keys[pygame.K_a]:
                    action = 12  # LEFTFIRE
                elif keys[pygame.K_s]:
                    action = 13  # DOWNFIRE
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE (basic punch)
            elif game_name == 'DemonAttack':
                # Basic movements
                if keys[pygame.K_LEFT]:
                    action = 3  # LEFT
                elif keys[pygame.K_RIGHT]:
                    action = 2  # RIGHT
                
                # Fire combinations
                if keys[pygame.K_a]:
                    action = 5  # LEFTFIRE
                elif keys[pygame.K_d]:
                    action = 4  # RIGHTFIRE
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE
            elif game_name == 'DoubleDunk':
                # Basic movements
                if keys[pygame.K_UP]:
                    action = 2  # UP
                elif keys[pygame.K_RIGHT]:
                    action = 3  # RIGHT
                elif keys[pygame.K_LEFT]:
                    action = 4  # LEFT
                elif keys[pygame.K_DOWN]:
                    action = 5  # DOWN
                
                # Diagonal movements
                if keys[pygame.K_e]:
                    action = 6  # UPRIGHT
                elif keys[pygame.K_q]:
                    action = 7  # UPLEFT
                elif keys[pygame.K_c]:
                    action = 8  # DOWNRIGHT
                elif keys[pygame.K_z]:
                    action = 9  # DOWNLEFT
                
                # Shoot combinations
                if keys[pygame.K_w]:
                    action = 10  # UPFIRE
                elif keys[pygame.K_d]:
                    action = 11  # RIGHTFIRE
                elif keys[pygame.K_a]:
                    action = 12  # LEFTFIRE
                elif keys[pygame.K_s]:
                    action = 13  # DOWNFIRE
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE (basic shoot/select)
            elif game_name == 'Enduro':
                # Basic movements
                if keys[pygame.K_RIGHT]:
                    action = 2  # RIGHT
                elif keys[pygame.K_LEFT]:
                    action = 3  # LEFT
                elif keys[pygame.K_DOWN]:
                    action = 4  # DOWN (Brake)
                
                # Combined movements
                if keys[pygame.K_c]:
                    action = 5  # DOWNRIGHT
                elif keys[pygame.K_z]:
                    action = 6  # DOWNLEFT
                
                # Acceleration combinations
                if keys[pygame.K_d]:
                    action = 7  # RIGHTFIRE
                elif keys[pygame.K_a]:
                    action = 8  # LEFTFIRE
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE (Accelerate)
            else:
                # Default controls for other games
                if keys[pygame.K_LEFT]:
                    action = 3  # LEFT
                elif keys[pygame.K_RIGHT]:
                    action = 2  # RIGHT
                elif keys[pygame.K_UP]:
                    action = 2  # UP
                elif keys[pygame.K_DOWN]:
                    action = 5  # DOWN
                elif keys[pygame.K_SPACE]:
                    action = 1  # FIRE
            
            # Execute action
            _, _, terminated, truncated, _ = env.step(action)
            
            if terminated or truncated:
                _, _ = env.reset()
        
        env.close()
        pygame.quit()
        
    except Exception as e:
        print(f"Error playing game: {e}")
        input("Press Enter to continue...")

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
