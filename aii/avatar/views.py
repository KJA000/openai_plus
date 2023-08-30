from django.shortcuts import render, redirect
from .forms import AvatarCustomizationForm

def avatar_customization(request):
    if request.method == "POST":
        form = AvatarCustomizationForm(request.POST)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect('mypage')  # or any other page you want them to go to
    else:
        form = AvatarCustomizationForm()
    return render(request, 'avatar/avatar_customization.html', {'form': form})
