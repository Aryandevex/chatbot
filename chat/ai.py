# chat/ai.py

from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

def get_ai_response(message):
    result = chatbot(message, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']