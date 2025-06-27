# Ricoso Voice Bot

This project is a Spanish-speaking AI voice bot for in-store child interaction.

## Tech Stack
- **API**: FastAPI
- **Speech-to-Text (STT)**: OpenAI Whisper
- **Natural Language Processing (NLP)**: spaCy
- **Text-to-Speech (TTS)**: pyttsx3

## Setup

1.  **Clone the repository:**
    ```bash
    https://github.com/LeoIvin/Rosco-VoiceBot
    cd Rosco-VoiceBot
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download spaCy Spanish model:**
    ```bash
    python -m spacy download es_core_news_sm
    ```
5. **Install ffmpeg:**
    Whisper requires ffmpeg to be installed on your system. You can install it using your system's package manager.
    - On macOS: `brew install ffmpeg`
    - On Debian/Ubuntu: `sudo apt-get install ffmpeg`
    - On Windows: Download from the official site and add to PATH.


## Running the Application

1.  **Start the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```

2.  **Access the API:**
    The API will be running at `http://127.0.0.1:8000`. You can access the documentation at `http://127.0.0.1:8000/docs`.

## Usage

You can interact with the bot by sending a POST request to the `/interact/` endpoint with a `.wav` audio file.

Example using `curl`:
```bash
curl -X POST -F "audio=@/path/to/your/audio.wav" http://127.0.0.1:8000/interact/ > response.wav
``` 