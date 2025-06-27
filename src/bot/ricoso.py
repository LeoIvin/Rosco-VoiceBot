from src.stt.whisper_stt import transcribe_audio
from src.nlp.spacy_nlp import process_text
from src.tts.pyttsx3_tts import text_to_speech
from src.utils.logger import log_conversation

def run_conversation_turn(audio_file):
    """
    Runs a single turn of the conversation.
    """
    # 1. Transcribe audio to text
    user_input = transcribe_audio(audio_file)
    log_conversation("Child", user_input)

    # 2. Process text to get bot response
    bot_response_text = process_text(user_input)
    log_conversation("Ricoso", bot_response_text)

    # 3. Convert bot response to speech
    output_audio_path = text_to_speech(bot_response_text)

    return output_audio_path 