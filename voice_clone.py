
import os
from TTS.api import TTS

print("Loading Models...")
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

reference_audio = 'cv.wav'

if not os.path.exists(reference_audio):
    print("Audio not found!")  
    exit()

# Ask user for input text
user_text = input("\nEnter your text to clone: ") 
clone_audio = "output.wav"

print("\nGenerating your cloned audio...")
tts.tts_to_file(
    text=user_text,
    speaker_wav=reference_audio,
    file_path=clone_audio,
    language='en'
)

print("\nYour text has been cloned! Saved as 'output.wav'.")

