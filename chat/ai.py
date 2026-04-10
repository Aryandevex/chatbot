import os
from huggingface_hub import InferenceClient
from transformers import pipeline

# -------------------------------
# Local chatbot model
# -------------------------------
chatbot = pipeline("text-generation", model="gpt2")

# -------------------------------
# HuggingFace client
# -------------------------------
client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ.get("HF_TOKEN"),
)

# -------------------------------
# Chatbot with CONTEXT support
# -------------------------------
def get_ai_response(context):
    result = chatbot(
        context,
        max_length=120,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )

    output = result[0]["generated_text"]

    # return only latest bot reply
    if "Bot:" in output:
        return output.split("Bot:")[-1].strip()

    return output.strip()


# -------------------------------
# Sentiment Analysis
# -------------------------------
def get_sentiment(message):
    result = client.text_classification(
        message,
        model="finiteautomata/bertweet-base-sentiment-analysis",
    )

    top = result[0]

    return {
        "label": top["label"],
        "score": round(top["score"], 2)
    }


# -------------------------------
# Summarization
# -------------------------------
def get_summary(message):
    result = client.summarization(
        message,
        model="csebuetnlp/mT5_multilingual_XLSum",
    )

    return result.summary_text