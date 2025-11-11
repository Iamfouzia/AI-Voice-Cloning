#this is not part of project code.This is extra for my understanding


# import os
# # Set model paths (must be before importing TTS)
# os.environ["TTS_MODEL_PATH"] = "E:\\TTS\\models"
# os.environ["TTS_VC_MODEL_PATH"] = "E:\\TTS\\models\\voice_conversion_models"

# import ffmpeg
# from TTS.api import TTS

# # Convert cv.opus → cv.wav if needed
# input_file = "cv.opus"
# output_file = "cv.wav"

# if not os.path.exists(output_file):
#     print("Converting cv.opus → cv.wav ...")
#     ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)
#     print("Conversion complete!")
# else:
#     print("cv.wav already exists, skipping conversion.")

# # Load TTS model
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True, gpu=False)

# # Voice cloning
# text = "Hello, I am Fouzia Khan's cloned voice speaking from the AI model. How are you?"
# speaker_wav = output_file
# output_path = "cloned_voice.wav"
# speaker = "female-en-5"
# language = "en"

# print("Voice cloned successfully! File saved as:", output_path)






