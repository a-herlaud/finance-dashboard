from dotenv import load_dotenv
import os
from litellm import completion

load_dotenv()

def llm_call(prompt: str):
    response = completion(
        model="gemini/gemini-3.1-flash-lite",
        api_key=os.getenv("GEMINI_API_KEY"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content