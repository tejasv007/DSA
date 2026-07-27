import whisper

model = whisper.load_model("base")
result = model.transcribe("voice.mp4")  # just pass the mp3 file
print(result["text"])