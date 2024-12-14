import simpleaudio as sa
import os

class SoundManager:
    def __init__(self):
        try:
            # Get the directory where sound.py is located
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up one level to project root and then into sounds directory
            sounds_dir = os.path.join(current_dir, '..', 'sounds')
            
            # Load built-in arcade sounds
            self.sounds = {
                'jump': sa.WaveObject.from_wave_file(os.path.join(sounds_dir, 'jump.wav')),
                'coin': sa.WaveObject.from_wave_file(os.path.join(sounds_dir, 'coin.wav')),
                'fire': sa.WaveObject.from_wave_file(os.path.join(sounds_dir, 'fire.wav')),
                'death': sa.WaveObject.from_wave_file(os.path.join(sounds_dir, 'death.wav')),
                'punch': sa.WaveObject.from_wave_file(os.path.join(sounds_dir, 'punch.wav')),
                'kick': sa.WaveObject.from_wave_file(os.path.join(sounds_dir, 'kick.wav'))
            }
            self.enabled = True
        except Exception as e:
            print(f"Warning: Sound initialization failed: {e}")
            self.enabled = False
    
    def load_game_sounds(self, game_name):
        # No need to load game-specific sounds anymore
        pass
    
    def play(self, sound_name):
        if self.enabled and sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except Exception as e:
                print(f"Warning: Could not play sound {sound_name}: {e}")
