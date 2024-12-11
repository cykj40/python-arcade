import gymnasium as gym
import os
import ale_py

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_available_games():
    games = {}
    game_list = [
        ('ALE/SpaceInvaders-v5', 'Space Invaders'),
        ('ALE/Pong-v5', 'Pong'),
        ('ALE/Breakout-v5', 'Breakout'),
        ('ALE/Asteroids-v5', 'Asteroids'),
        ('ALE/MsPacman-v5', 'Ms. Pacman'),
        ('ALE/BattleZone-v5', 'Battle Zone'),
        ('ALE/Boxing-v5', 'Boxing'),
        ('ALE/DemonAttack-v5', 'Demon Attack'),
        ('ALE/DoubleDunk-v5', 'Double Dunk'),
        ('ALE/Enduro-v5', 'Enduro'),
        ('ALE/DonkeyKong-v5', 'Donkey Kong'),
        ('ALE/KungFuMaster-v5', 'Kung Fu Master'),
        ('ALE/MarioBros-v5', 'Mario Bros')
    ]
    
    for i, (env_id, name) in enumerate(game_list, 1):
        games[str(i)] = {
            'name': name,
            'id': env_id
        }
    return games

def display_menu(games):
    print("\n=== Atari Arcade ===")
    print("\nAvailable Games:")
    for num, game in games.items():
        print(f"{num}. {game['name']}")
    print("\nQ. Quit")
    return input("\nSelect a game number (or Q to quit): ").upper()

def play_game(game_id, game_name):
    try:
        import pygame
        pygame.init()
        
        # Create environment with both human rendering and RGB array
        env = gym.make(game_id, render_mode="human", full_action_space=False)
        _, info = env.reset()
        
        # Get the legal actions from the ALE environment
        legal_actions = env.unwrapped.ale.getLegalActionSet()
        action_meanings = env.unwrapped.get_action_meanings()
        
        print(f"\nPlaying {game_name}")
        print("Controls:")
        print("Available actions:", action_meanings)
        print("Press ESC to return to menu")
        
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
            
            # Map keyboard input to legal actions
            action = 0  # NOOP is usually 0
            
            # Basic movements
            if keys[pygame.K_LEFT] and keys[pygame.K_UP] and 'UPLEFT' in action_meanings:
                action = legal_actions[action_meanings.index('UPLEFT')]
            elif keys[pygame.K_RIGHT] and keys[pygame.K_UP] and 'UPRIGHT' in action_meanings:
                action = legal_actions[action_meanings.index('UPRIGHT')]
            elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and 'DOWNLEFT' in action_meanings:
                action = legal_actions[action_meanings.index('DOWNLEFT')]
            elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and 'DOWNRIGHT' in action_meanings:
                action = legal_actions[action_meanings.index('DOWNRIGHT')]
            # Combined fire actions
            elif keys[pygame.K_SPACE]:
                if keys[pygame.K_UP] and 'UPFIRE' in action_meanings:
                    action = legal_actions[action_meanings.index('UPFIRE')]
                elif keys[pygame.K_RIGHT] and 'RIGHTFIRE' in action_meanings:
                    action = legal_actions[action_meanings.index('RIGHTFIRE')]
                elif keys[pygame.K_LEFT] and 'LEFTFIRE' in action_meanings:
                    action = legal_actions[action_meanings.index('LEFTFIRE')]
                elif keys[pygame.K_DOWN] and 'DOWNFIRE' in action_meanings:
                    action = legal_actions[action_meanings.index('DOWNFIRE')]
                elif 'FIRE' in action_meanings:
                    action = legal_actions[action_meanings.index('FIRE')]
            # Single direction movements
            elif keys[pygame.K_LEFT] and 'LEFT' in action_meanings:
                action = legal_actions[action_meanings.index('LEFT')]
            elif keys[pygame.K_RIGHT] and 'RIGHT' in action_meanings:
                action = legal_actions[action_meanings.index('RIGHT')]
            elif keys[pygame.K_UP] and 'UP' in action_meanings:
                action = legal_actions[action_meanings.index('UP')]
            elif keys[pygame.K_DOWN] and 'DOWN' in action_meanings:
                action = legal_actions[action_meanings.index('DOWN')]
            
            _, reward, terminated, truncated, info = env.step(action)
            
            if terminated or truncated:
                print(f"Game Over! Score: {info.get('score', 0)}")
                print(f"Final Reward: {reward}")
                break
        
        env.close()
        pygame.quit()
        input("\nPress Enter to continue...")
        
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to continue...")

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