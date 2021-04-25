from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from django.http import Http404
from django.views import generic
from .forms import RegisterForm
from django.contrib.auth import login, authenticate


def list(request):
    ls = Book.objects.all()
    return render(request, "music/list.html", {"ls": ls})


def index(request, id):
   try:
       ls = Book.objects.get(pk=id)
   except Book.DoesNotExist:
       raise Http404("Book Does Not Exist")
   return render(request, "music/info.html", {"ls": ls})


def home(request):
    return render(request, "music/home.html")


def register(request):
    if request.method == "POST":
	     form = RegisterForm(request.POST)
	     if form.is_valid():
              form.save()
              username = form.cleaned_data.get('username')
              raw_password = form.cleaned_data.get('password')
              user = authenticate(username=username, password=raw_password)
              login(request, user)
           
	     return redirect("/home")
    else:
	    form = RegisterForm()

    return render(request, "music/signup.html", {"form":form})
   


   #for login
    # test case1 username=user3 and password=pass123@
    # test case2 username=admin and password=admin
   
def searchbook(request):
    if request.method == "POST":
        searched = request.POST['searched']
        ls = Book.objects.filter(title__contains=searched)

        return render(request,'music/searchbook.html',{"ls":ls,"searched":searched})