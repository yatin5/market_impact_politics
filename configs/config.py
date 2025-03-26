from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

# Validate API keys
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY is not set in the environment variables.")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
if not GOOGLE_CSE_ID:
    raise ValueError("GOOGLE_CSE_ID is not set in the environment variables.")

print("[Config] API keys loaded successfully.")
print("[Config] Google API key and CSE ID loaded successfully.")