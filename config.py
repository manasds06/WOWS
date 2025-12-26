
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This reads the .env file and makes variables accessible via os.getenv()
load_dotenv()

# =============================================================================
# API KEYS (Required)
# =============================================================================

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def validateConfig():
    missing_keys = []
    
    if not NEWS_API_KEY:
        missing_keys.append("NEWS_API_KEY")
    
    if not GEMINI_API_KEY:
        missing_keys.append("GEMINI_API_KEY")
    
    if missing_keys:
        raise ValueError(
            f"Missing required API keys in .env file"
        )
    
    print("success")