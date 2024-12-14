import requests
from dotenv import load_dotenv
import os
import sys


# Load environment variables from .env file
load_dotenv()
# Access the API key
API_TOKEN = os.getenv("API_KEY")
MODEL_NAME = sys.argv[1]

# Define the API URL
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

# Input text prompt
text_prompt = sys.argv[2]

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# JSON payload
payload = {
    "inputs": text_prompt,
}

# Make the request
response = requests.post(API_URL, headers=headers, json=payload)

# Handle the response
if response.status_code == 200:
    # Save the audio file
    with open(".generated_audio.wav", "wb") as audio_file:
        audio_file.write(response.content)
    print("Audio generated and saved as 'generated_audio.wav'")
else:
    print(f"Error: {response.status_code}, {response.text}")
