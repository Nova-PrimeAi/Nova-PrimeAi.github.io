import os
from google import genai
from dotenv import load_dotenv

# 1. Load environment variables from a .env file
load_dotenv()

# 2. Get the API Key
API_KEY = os.getenv("nah bro you are not getting it")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please add it to your .env file.")

# 3. Initialize the Gemini Client
client = genai.Client(api_key=API_KEY)

def chat_with_gemini():
    print("--- Gemini 2.5 Flash AI Active ---")
    user_input = input("You: ")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        print(f"\nGemini: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_gemini()
