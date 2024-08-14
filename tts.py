from pathlib import Path
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Paths for input and output
input_text_file = Path(__file__).parent / "voice.txt"
output_folder = Path(__file__).parent / "voiceover"
output_folder.mkdir(exist_ok=True)
output_file_path = output_folder / "voiceover.mp3"

# Read the input text from the file
with open(input_text_file, 'r') as file:
    text = file.read()

try:
    # Generate text-to-speech using OpenAI's API and save the audio to a file
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    
    # Save the response content directly to the file
    with open(output_file_path, 'wb') as f:
        f.write(response.content)  # Assuming 'content' contains the audio data
    
    print(f"Voiceover generated and saved to {output_file_path}")
except OpenAIError as e:
    print(f"An error occurred: {e}")
