from django.shortcuts import render, redirect
from .forms import ReguserForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
# Create your views here.

def reguser(response):
    if response.method == "POST":
        form = ReguserForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ReguserForm()

    return render(response, "reguser/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
