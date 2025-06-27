from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from src.bot.ricoso import run_conversation_turn

app = FastAPI()

# Create a directory for temporary audio files
os.makedirs("temp_audio", exist_ok=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/interact/")
async def interact(audio: UploadFile = File(...)):
    """
    Endpoint to interact with the bot.
    Receives an audio file, processes it, and returns the bot's audio response.
    """
    temp_audio_path = f"temp_audio/{audio.filename}"
    with open(temp_audio_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    output_audio_path = run_conversation_turn(temp_audio_path)

    return FileResponse(output_audio_path, media_type="audio/wav") 