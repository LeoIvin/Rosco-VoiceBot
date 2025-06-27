import pyttsx3
import os
import time

# Create a directory for TTS output files
os.makedirs("tts_output", exist_ok=True)

def text_to_speech(text):
    """
    Converts text to speech using pyttsx3 and saves it to a file.
    """
    engine = pyttsx3.init()

    # Set properties for Spanish voice
    voices = engine.getProperty('voices')
    # Note: You might need to experiment with the voice ID on your system.
    # You can loop through `voices` and print `v.id` and `v.name` to find a Spanish one.
    # For now, we'll try to find a Spanish voice by name.
    spanish_voice_id = None
    for voice in voices:
        if 'spanish' in voice.name.lower() or 'español' in voice.name.lower():
            spanish_voice_id = voice.id
            break

    if spanish_voice_id:
        engine.setProperty('voice', spanish_voice_id)
    else:
        print("Spanish voice not found, using default.")

    engine.setProperty('rate', 150)  # Speed of speech

    # Generate a unique filename
    output_filename = f"tts_output/response_{int(time.time())}.wav"
    
    print(f"Converting text to speech: {text}")
    engine.save_to_file(text, output_filename)
    engine.runAndWait()
    
    return output_filename 