import os
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
    SpeakOptions
)

load_dotenv()
deepgram = DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))

def text_to_speech(question_text, filename="question.mp3"):
    try:
        options = SpeakOptions(model="aura-orpheus-en")
        TEXT = {"text": question_text }
        response = deepgram.speak.rest.v("1").stream(TEXT, options)

        print(response)
    except Exception as e:
        raise e

# Transcribe user response audio to text.
def speech_to_text(audio_file):
    with open(audio_file, "rb") as file:
        buffer_data = file.read()

    payload: FileSource = {"buffer": buffer_data}

    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True,
        filler_words=True
    )

    # Get the transcription response from Deepgram
    response = deepgram.listen.rest.v("1").transcribe_file(payload, options)
    transcription = response.to_dict()
    transcript = transcription['results']['channels'][0]['alternatives'][0]['transcript']
    confidence = transcription['results']['channels'][0]['alternatives'][0]['confidence']
    print(f"Transcription Confidence: {confidence}")

    return transcript

# if transcript:
#     # Step 3: Append user's response to the conversation history
#     conversation_history.append({"role": "user", "content": transcript})

#     # Generate the next question based on the updated conversation history
#     next_question = generate_next_question(conversation_history)
#     print(f"Groq: {next_question}")

#     # Convert the next question to speech
#     text_to_speech(next_question, "next_question.mp3")

#     # Repeat the process (you can loop this in a real-world scenario)
# else:
#     print("User response not transcribed!")

