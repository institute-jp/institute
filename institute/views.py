from django.shortcuts import  render, redirect
from .forms import RegisterForm, CreateMember
from django.contrib.auth.decorators import login_required

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(response, "institute/register.html", {"form":form})

@login_required(login_url="/accounts/login/")
def create(request):
    if request.method == "POST":
        form = CreateMember(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.member = request.user
            instance.save()
    else:
        form = CreateMember()
    return render(request, "institute/create.html", {"form":form})
    


