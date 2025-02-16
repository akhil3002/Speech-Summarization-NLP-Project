import whisper

def transcribe_with_whisper(audio_file):
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    print("Transcribing with Whisper...")
    result = model.transcribe(audio_file)
    return result["text"]
