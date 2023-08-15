import openai
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Message
from .forms import ChatForm

openai.api_key = settings.OPENAI_API_KEY


def generate_response():
    messages = [{"role": message.role, "content": message.content} for message in Message.objects.all()]

    steve_jobs_prompt = {
        "role": "system",
        "content": "Act as Steve Jobs. Respond like in the situation of online chat to the input."
    }
    if steve_jobs_prompt not in messages:
        messages.insert(0, steve_jobs_prompt)

    gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )
    
    return gpt_response["choices"][0]["message"]["content"]

def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        
        if 'clear_messages' in request.POST:
            Message.objects.all().delete()
            return redirect('steve') 
        
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            
            user_message = Message(role="user", content=user_input)
            user_message.save()
            
            response_content = generate_response()
            
            response_message = Message(role="assistant", content=response_content)
            response_message.save()
            
            return redirect('steve')  

    else:
        form = ChatForm()

    messages = Message.objects.all()
    return render(request, 'openai_api.html', {'form': form, 'messages': messages})
