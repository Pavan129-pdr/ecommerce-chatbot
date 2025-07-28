from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import queries

app = FastAPI()

# 👇 Add this CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"] to be more specific
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
def chat(input: ChatInput):
    message = input.message.lower()

    if "order" in message:
        import re
        match = re.search(r"\b\d{4,6}\b", message)
        if match:
            order_id = int(match.group())
            return queries.get_order_status(order_id)

    elif "top" in message:
        return queries.get_top_products()

    elif "stock" in message:
        words = message.split()
        for word in words:
            if word.isalpha():
                return queries.get_stock(word)

    return {"response": "Sorry, I didn't understand your request."}
