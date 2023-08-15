from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(label="Enter your message", max_length=1000)
