import simpleaudio as sa
import os

class SoundManager:
    def __init__(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(current_dir)
            sounds_dir = os.path.join(project_root, 'sounds')
            
            # Map ALE actions to sounds
            self.action_sounds = {
                'NOOP': None,
                'FIRE': 'fire',
                'UP': 'jump',
                'RIGHT': None,
                'LEFT': None,
                'DOWN': None,
                'UPRIGHT': 'jump',
                'UPLEFT': 'jump',
                'DOWNRIGHT': None,
                'DOWNLEFT': None,
                'UPFIRE': 'fire',
                'RIGHTFIRE': 'fire',
                'LEFTFIRE': 'fire',
                'DOWNFIRE': 'fire',
                'UPRIGHTFIRE': 'fire',
                'UPLEFTFIRE': 'fire',
                'DOWNRIGHTFIRE': 'fire',
                'DOWNLEFTFIRE': 'fire'
            }
            
            # Load sound files
            self.sounds = {}
            sound_files = ['coin', 'death', 'fire', 'jump', 'kick', 'punch']
            
            for sound in sound_files:
                sound_path = os.path.join(sounds_dir, f'{sound}.wav')
                if os.path.exists(sound_path):
                    try:
                        self.sounds[sound] = sa.WaveObject.from_wave_file(sound_path)
                        print(f"Successfully loaded: {sound}.wav")
                    except Exception as e:
                        print(f"Failed to load {sound}.wav: {e}")
            
            self.enabled = len(self.sounds) > 0
            
        except Exception as e:
            print(f"Warning: Sound initialization failed: {e}")
            self.enabled = False
    
    def play(self, sound_name):
        """Play a sound by name"""
        if not self.enabled or sound_name not in self.sounds:
            return
        try:
            self.sounds[sound_name].play()
        except Exception as e:
            print(f"Warning: Could not play sound {sound_name}: {e}")
    
    def play_for_action(self, action, game_name):
        """Play appropriate sound for the given ALE action"""
        if not self.enabled:
            return
            
        # Map action numbers to names
        action_map = {
            0: 'NOOP',
            1: 'FIRE',
            2: 'UP',
            3: 'RIGHT',
            4: 'LEFT',
            5: 'DOWN',
            6: 'UPRIGHT',
            7: 'UPLEFT',
            8: 'DOWNRIGHT',
            9: 'DOWNLEFT',
            10: 'UPFIRE',
            11: 'RIGHTFIRE',
            12: 'LEFTFIRE',
            13: 'DOWNFIRE',
            14: 'UPRIGHTFIRE',
            15: 'UPLEFTFIRE',
            16: 'DOWNRIGHTFIRE',
            17: 'DOWNLEFTFIRE'
        }
        
        action_name = action_map.get(action)
        if action_name:
            sound_name = self.action_sounds.get(action_name)
            if sound_name:
                if game_name in ['Boxing', 'KungFuMaster'] and 'FIRE' in action_name:
                    self.play('punch')
                elif game_name in ['MarioBros', 'DonkeyKong'] and 'UP' in action_name:
                    self.play('jump')
                else:
                    self.play(sound_name)
