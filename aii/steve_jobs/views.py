import openai
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Message
from .forms import ChatForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

openai.api_key = settings.OPENAI_API_KEY

def generate_response(request):
    messages = [{"role": message.role, "content": message.content} for message in Message.objects.filter(user=request.user)]

    steve_jobs_prompt = {
        "role": "system",
        "content": "You are Steve Jobs. Respond like Steve Jobs in the situation of online chat to the input."
    }
    if steve_jobs_prompt not in messages:
        messages.insert(0, steve_jobs_prompt)

    gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )
    
    return gpt_response["choices"][0]["message"]["content"]

@login_required
def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        
        if 'clear_messages' in request.POST:
            Message.objects.filter(user=request.user).delete()
            return redirect('steve') 
        
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            
            user_message = Message(role="user", content=user_input, user=request.user)
            user_message.save()
            
            response_content = generate_response(request)
            
            response_message = Message(role="assistant", content=response_content, user=request.user)
            response_message.save()
            
            return redirect('steve')  

    else:
        form = ChatForm()

    messages = Message.objects.filter(user=request.user)
    return render(request, 'openai_api.html', {'form': form, 'messages': messages})
