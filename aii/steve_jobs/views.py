import openai
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Message
from .forms import ChatForm
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_response(user_input):
    gpt_prompt = [
        {
            "role": "system",
            "content": "Act as Steve Jobs. Respond like in the situation of online chat to the input.",
        },
        {"role": "user", "content": user_input}
    ]

    gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=gpt_prompt
    )
    
    return gpt_response["choices"][0]["message"]["content"]

def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            
            user_message = Message(role="user", content=user_input)
            user_message.save()
            
            response_content = generate_response(user_input)
            response_message = Message(role="Steve Jobs", content=response_content)
            response_message.save()
            
            return redirect('steve')  

    else:
        form = ChatForm()

    messages = Message.objects.all()
    return render(request, 'openai_api.html', {'form': form, 'messages': messages})