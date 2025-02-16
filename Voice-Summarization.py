from voice_to_text import transcribe_with_whisper
from text_summarization import summarize_long_text
from text_to_speech import text_to_speech

def main():
    # Step 1: Voice to Text
    audio_file = "C:\\Users\\akhil\\Desktop\\Voice-Summarization\\winston-churchill-the-threat-of-germany.wav"
    print("Step 1: Transcribing audio...")
    transcription = transcribe_with_whisper(audio_file)
    print("Transcription Done!")
    print("Transcription\n")
    print(transcription)
    #Save transcription 
    output_file = "Original_text.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(transcription)
    print(f"\nTranscription text has been saved to'{output_file}'.")
    # Step 2: Text Summarization
    print("\nStep 2: Summarizing transcription...")
    summarized_text = summarize_long_text(transcription, max_chunk_size=1024, max_length=130, min_length=30)
    print("Summarization Done!")
    print("Summarized Text\n")
    print(summarized_text)
    #Save summarized text to a file
    output_file = "summarized_text.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(summarized_text)
    print(f"\nSummarized text has been saved to'{output_file}'.")
    # Step 3: Text to Speech
    print("\nStep 3: Converting summary to speech...")
    text_to_speech(summarized_text)

if __name__ == "__main__":
    main()
