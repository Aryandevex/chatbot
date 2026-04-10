from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .ai import get_ai_response, get_sentiment, get_summary


# -------------------------------
# Chat Page
# -------------------------------
@login_required
def chat_view(request):
    return render(request, "chat.html")


# -------------------------------
# CHATBOT (WITH MEMORY)
# -------------------------------
@login_required
def get_response(request):
    message = request.GET.get("message", "")

    # get history from session
    history = request.session.get("chat_history", [])

    # add user message
    history.append(f"User: {message}")

    # build context for model
    context = "\n".join(history) + "\nBot:"

    # get response using full context
    reply = get_ai_response(context)

    # store bot reply
    history.append(f"Bot: {reply}")

    # keep last 10 messages only
    request.session["chat_history"] = history[-10:]

    return JsonResponse({"response": reply})


# -------------------------------
# SENTIMENT
# -------------------------------
@login_required
def sentiment_view(request):
    message = request.GET.get("message", "")
    reply = get_sentiment(message)
    return JsonResponse({"response": reply})


# -------------------------------
# SUMMARY
# -------------------------------
@login_required
def summary_view(request):
    message = request.GET.get("message", "")
    reply = get_summary(message)
    return JsonResponse({"response": reply})