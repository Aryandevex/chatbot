from transformers import pipeline

# Models
chatbot = pipeline("text-generation", model="gpt2")
sentiment_pipeline = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")

def get_ai_response(message):
    result = chatbot(message, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']


def get_sentiment(message):
    result = sentiment_pipeline(message)[0]
    return f"{result['label']} ({round(result['score'], 2)})"


def get_summary(message):
    result = summarizer(message, max_length=50, min_length=10, do_sample=False)
    return result[0]['summary_text']
