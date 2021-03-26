from django.shortcuts import  render, redirect
from .forms import RegisterForm, CreateMember, GeneralDegreeForm, MbaForm
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
        member_form = CreateMember(request.POST)
        general_degree_form = GeneralDegreeForm(request.POST)
        mba_form = MbaForm(request.POST)

        if member_form.is_valid() and general_degree_form.is_valid() and mba_form.is_valid():
            member_instance = member_form.save(commit=False)
            member_instance.member = request.user
            member_instance.save()
            general_degree_instance = general_degree_form.save(commit=False)
            general_degree_instance.member = request.user
            general_degree_instance.save()
            mba_instance = mba_form.save(commit=False)
            mba_instance.member = request.user
            mba_instance.save()
    else:
        member_form = CreateMember()
        general_degree_form = GeneralDegreeForm()
        mba_form = ModelForm()
    return render(request, "institute/create.html", {"member_form":member_form, "general_degree_form":general_degree_form, "mba_form":mba_form})
    


