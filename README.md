# python-arcade

A Python-based Atari game emulator using the Arcade Learning Environment (ALE) and Gymnasium.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install required packages:
```bash
pip install ale-py
pip install gymnasium[atari]
pip install 'gymnasium[accept-rom-license]'
pip install pygame
pip install simpleaudio
```

## Running the Games

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the game:
```bash
python -m my_arcade.test_env
```

## Global Controls
- ESC: Return to menu
- Q: Quit game

## Game-Specific Controls

### Space Invaders
- Left/Right: Move
- Space: Fire
- A/D: Move and fire

### Pong
- Up/Down: Move paddle
- Space: Serve ball
- W/S: Move and serve

### Breakout
- Left/Right: Move paddle
- Space: Launch ball

### Asteroids
- Arrow keys: Rotate and thrust
- Space: Fire
- E/Q: Thrust diagonally
- W: Thrust and fire
- A/D: Rotate and fire
- S: Reverse thrust and fire
- R/F: Diagonal thrust and fire

### BattleZone
- Arrow keys: Tank movement
- Space: Fire cannon
- E/Q: Forward diagonal movement
- C/Z: Backward diagonal movement
- W/S: Forward/Backward with fire
- A/D: Rotate and fire

### Boxing
- Arrow keys: Movement
- Space: Punch
- E/Q: Move up-diagonally
- C/Z: Move down-diagonally
- W/A/S/D: Move and punch

### DemonAttack
- Left/Right: Move
- Space: Fire laser
- A/D: Move and fire

### DoubleDunk
- Arrow keys: Movement
- Space: Shoot/Select play
- E/Q: Move up-diagonally
- C/Z: Move down-diagonally
- W/A/S/D: Move and shoot

### Enduro
- Left/Right: Steer
- Down: Brake
- Space: Accelerate
- C/Z: Brake and steer
- A/D: Accelerate and steer

### DonkeyKong
- Left/Right: Move
- Space: Jump
- Enter: Start/Hammer

### KungFuMaster
- Left/Right: Move
- Up: Jump
- Down: Crouch
- Space: Punch/Kick
- A/D: Directional attacks
- Q/E: Jump attacks
- Z/C: Crouch attacks

### MarioBros
- Arrow keys: Movement
- Space: Jump
- Q/E: Jump diagonally
- Z/C: Crouch and move
- W/A/S/D: Combined moves

## Dependencies
- ALE (Arcade Learning Environment) - GPL-2.0 License
- Gymnasium - MIT License
- Atari ROMs - Requires separate licensing

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Citations
This project uses the Arcade Learning Environment (ALE). If you use this software in your research, please cite: 
bibtex
@Article{bellemare13arcade,
author = {{Bellemare}, M.~G. and {Naddaf}, Y. and {Veness}, J. and {Bowling}, M.},
title = {The Arcade Learning Environment: An Evaluation Platform for General Agents},
journal = {Journal of Artificial Intelligence Research},
year = "2013",
month = "jun",
volume = "47",
pages = "253--279",
}