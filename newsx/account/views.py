from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:items')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form })

def login_view(request):
    if request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles:items')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:items')