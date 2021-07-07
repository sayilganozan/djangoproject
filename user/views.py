from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm


from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout


from django.contrib import messages
# Create your views here.

def register(request):


    form = RegisterForm(request.POST or None) # methodun postmu getmi oldugunu böylece kntrol etmek zorunda kalmıyoruz.
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")


        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)

        messages.success(request,"Başarıyla sisteme kayıt oldunuz..")
        #messages.error(request,"!!! Başarıyla sisteme kayıt oldunuz..")
            
        return redirect("index")

    context ={
        
    "form":form

        }
    return render(request,"register.html",context)  



def loginUser(request):


    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.error(request,"Kullanıcı adı veya parola hatalı..")
            return render(request,"login.html",context)


        messages.success(request,"Başarıyla sisteme giriş yaptınız.")
        login(request,user)  # kullanıcı sisteme giriş yaptı ve ana sayfaya yönlendirildi.

        return redirect("index")

    return render(request,"login.html",context)

def logoutUser(request):
    
    logout(request)

    messages.success(request,"Sistemden Başarıyla Çıkış Yaptınız..")

    return redirect("index")
