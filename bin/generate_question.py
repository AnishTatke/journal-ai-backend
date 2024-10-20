import os
from dotenv import load_dotenv
from groq import Groq

from models.History import History

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Generate the next question using Groq based on the conversation history.
def generate_next_question(history: History):
    hist = history.get_history()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=hist,
        temperature=0.7, 
        max_tokens=150,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    new_question = completion.choices[0].message.content
    return new_question

