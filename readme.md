# Text-to-Speech Conversion Using OpenAI API

This project demonstrates how to convert text into lifelike spoken audio using the OpenAI API. The script reads text from a file, converts it to speech using OpenAI's Text-to-Speech (TTS) model, and saves the output as an audio file.

## What is Text-to-Speech (TTS)?

Text-to-Speech (TTS) is a technology that converts written text into spoken words. It is widely used in applications like virtual assistants, accessibility tools, and audiobooks. The OpenAI TTS API provides a way to generate high-quality, AI-driven spoken audio from text inputs.

## Libraries and Imports

The following libraries are used in this project:

- `pathlib`: A standard Python library that offers an object-oriented approach to handling filesystem paths.
- `openai`: The official OpenAI Python client for interacting with their APIs.
- `dotenv`: A library that loads environment variables from a `.env` file into the Python environment.
- `os`: A standard Python library used for interacting with the operating system.

### Code Explanation

Here's a step-by-step breakdown of the code:

```python
from pathlib import Path
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import os
```

- `pathlib.Path`: Provides an easy way to manipulate filesystem paths.
- `OpenAI`: The main class for interacting with the OpenAI API.
- `OpenAIError`: An exception class for handling errors related to the OpenAI API.
- `load_dotenv`: Loads environment variables from a `.env` file into the environment.
- `os`: Provides a way to interact with the operating system, mainly used here for accessing environment variables.

### Loading Environment Variables

```python
# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
```

- `load_dotenv()`: Reads the `.env` file located in the same directory and loads the environment variables into the Python environment.
- `api_key`: Retrieves the OpenAI API key from the environment variables.
- `client`: Initializes the OpenAI client using the provided API key.

### File Paths for Input and Output

```python
# Paths for input and output
input_text_file = Path(__file__).parent / "voice.txt"
output_folder = Path(__file__).parent / "voiceover"
output_folder.mkdir(exist_ok=True)
output_file_path = output_folder / "voiceover.mp3"
```

- `input_text_file`: Specifies the path to the input text file (`voice.txt`) that contains the text to be converted to speech.
- `output_folder`: Specifies the directory where the output audio file will be saved. If the directory does not exist, it is created using `mkdir(exist_ok=True)`.
- `output_file_path`: Specifies the path to the output audio file (`voiceover.mp3`).

### Reading the Input Text

```python
# Read the input text from the file
with open(input_text_file, 'r') as file:
    text = file.read()
```

- The script reads the contents of the `voice.txt` file and stores it in the `text` variable.

### Generating Text-to-Speech

```python
try:
    # Generate text-to-speech using OpenAI's API and save the audio to a file
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
```

- The script sends a request to the OpenAI API to generate speech from the input text.
- `model="tts-1"`: Specifies the TTS model to be used. The `"tts-1"` model is chosen for this example.
- `voice="alloy"`: Specifies the voice to be used. The `"alloy"` voice is selected, but other voices like `"echo"`, `"fable"`, `"onyx"`, `"nova"`, and `"shimmer"` are also available.
- `input=text`: Passes the text read from the file as input to the TTS model.

### Saving the Generated Audio

```python
    # Save the response content directly to the file
    with open(output_file_path, 'wb') as f:
        f.write(response.content)  # Assuming 'content' contains the audio data
    
    print(f"Voiceover generated and saved to {output_file_path}")
```

- The generated audio is saved to the specified file path (`voiceover.mp3`).
- `response.content`: The binary content of the audio file is written to the output file.

### Error Handling

```python
except OpenAIError as e:
    print(f"An error occurred: {e}")
```

- This block catches any errors that may occur during the API call and prints a relevant error message.

## Environment Variables

The script uses a `.env` file to securely manage the OpenAI API key. The `.env` file should be placed in the same directory as the script and contain the following line:

```
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

## Input and Output Files

- **Input File**: The script reads text from `voice.txt`, which should be placed in the same directory as the script.
- **Output File**: The generated audio is saved as `voiceover.mp3` in the `voiceover` directory, which will be created if it doesn't exist.

## How to Run the Script

1. Install the required Python libraries:

   ```bash
   pip install openai python-dotenv
   ```

2. Place your OpenAI API key in a `.env` file in the same directory as the script.

3. Create a `voice.txt` file in the same directory with the text you want to convert to speech.

4. Run the script:

   ```bash
   python your_script_name.py
   ```

5. The output audio file will be saved as `voiceover.mp3` in the `voiceover` directory.

## Conclusion

This project is a simple demonstration of how to use the OpenAI API for converting text into speech. It covers loading environment variables, reading text from a file, generating speech using the OpenAI API, and saving the output to an audio file. This approach can be easily extended to handle more complex text-to-speech scenarios and integrated into larger applications.

