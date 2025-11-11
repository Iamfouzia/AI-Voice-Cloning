# AI Voice Cloning

## Project Overview
AI Voice Cloning is a Python project that clones a speaker's voice from a reference audio file and generates speech from user-provided text using the Coqui TTS library.  

## Features
- Clone any voice using a reference `.wav` file.  
- Generate output audio (`output.wav`) from typed text.  
- Supports multilingual TTS models.  

## Installation
1. Clone the repository:  
```bash
git clone https://github.com/Iamfouzia/AI-Voice-Cloning.git
cd AI-Voice-Cloning

2. Install required packages:
pip install TTS soundfile torch torchaudio

##Usage
1. Place your reference audio file (e.g., cv.wav) in the project folder.
2. Run the script:
python voice_clone.py
3. Enter the text you want to convert to speech.
4. The output audio will be saved as output.wav.

Files
--> voice_clone.py – Main Python script
--> cv.wav – Example reference audio
--> output.wav – Generated cloned audio

AI-Voice-Cloning/
├─ voice_clone.py       # Main Python script
├─ cv.wav               # Reference audio file
├─ output.wav           # Generated cloned audio
├─ requirements.txt     # Python dependencies
└─ README.md            # Project description

##How it Works
-->Loads a pre-trained multilingual TTS model from Coqui TTS.
-->Processes the reference audio file to capture the speaker's voice characteristics.
-->Converts the user’s text input into audio mimicking the reference speaker.

Enter your text to clone: Hello Fouzia Khan, this is my cloned voice!
Your text has been cloned! Saved as 'output.wav'.


