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

## Controls
- Arrow keys: Movement
- Space: Fire/Action
- ESC: Return to menu
- Q: Quit game

## Game-Specific Controls

### Donkey Kong
- Left/Right: Move
- Space: Jump
- Enter: Start/Hammer

### Kung Fu Master
- Left/Right: Move
- Up: Jump
- Down: Crouch
- Space: Punch/Kick
- A: Left Attack
- D: Right Attack

### Mario Bros
- Left/Right: Move
- Space: Jump
- Enter: Start

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