from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def chat_view(request):
    return render(request, "chat.html")


@login_required
def get_response(request):
    message = request.GET.get("message", "").lower()

    # Basic rule-based chatbot
    if "hello" in message:
        reply = "Hi 👋 How can I help you?"
    elif "how are you" in message:
        reply = "I'm just a bot, but I'm doing great 😄"
    elif "bye" in message:
        reply = "Goodbye! Have a nice day 😊"
    else:
        reply = "Sorry, I didn't understand that."

    return JsonResponse({"response": reply})

# from .ai import get_ai_response

# @login_required
# def get_response(request):
#     message = request.GET.get("message")

#     reply = get_ai_response(message)

#     return JsonResponse({"response": reply})