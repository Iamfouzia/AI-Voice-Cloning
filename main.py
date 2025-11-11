


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

# tts.tts_with_vc_to_file(
#     text=text,
#     speaker_wav=speaker_wav,
#     speaker=speaker,
#     language=language,
#     file_path=output_path
# )

# print("Voice cloned successfully! File saved as:", output_path)






# import os
# from TTS.api import TTS

# print("loading Models..")
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False,gpu=False)

# reference_audio ='cv.wav'

# if not os.path.exists(reference_audio):
#  print("audio not found")  
#  exit()
 
#  user_text = input("\nEnter your text for clone") 
#  clone_audio = "output.wav"
 
#  tts.tts_to_file(
#      text=user_text,
#      speaker_wav=reference_audio,
#      file_path=clone_audio,
#      language='en'
#  )
#  print("\nYour Text Clone Computer")
