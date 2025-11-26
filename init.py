from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
try:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    print ("GEMINI_API_KEY:", GEMINI_API_KEY)
    print("✅ API key setup complete.")
except KeyError:
    raise KeyError("GOOGLE_API_KEY not found in environment variables.")



client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)