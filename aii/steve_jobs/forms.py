from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(label="Enter your message", max_length=1000)

class FeedbackForm(forms.Form):
    RATINGS = (
        ('best', 'Best'),
        ('good', 'Good'),
        ('normal', 'Normal'),
        ('bad', 'Bad'),
        ('worst', 'Worst'),
    )
    rating = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect)