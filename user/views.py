from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from article.models import Article

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        password = form.cleaned_data.get("password")
        newUser = User(username=username, first_name=first_name,
            last_name=last_name)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Başarıyla Kayıt Oldunuz!")
        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Yanlış!")
            return render(request, "login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız!")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
    return render(request,'yazarlar.html',context)
def userdetail(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request,'user_detail.html',context)
