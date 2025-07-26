from fastapi import FastAPI
from pydantic import BaseModel
import queries

app = FastAPI()

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
