from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.views import serve


#Bypass 
from django.shortcuts import render, redirect
from .forms import BypassForm
from django.contrib.auth.decorators import login_required



# views.py
from django.shortcuts import render, redirect
from .forms import BypassForm

def bypass(request):
    if request.method == 'POST':
        form = BypassForm(request.POST, user=request.user)  # Transmite `user` la formular
        if form.is_valid():
            bypass = form.save(commit=False)
            bypass.utilizator = request.user
            bypass.save()
            return redirect('formular_bypass')  # Asigură-te că acest nume corespunde cu cel din urls.py
    else:
        form = BypassForm(user=request.user)  # Transmite `user` la formular

    return render(request, 'formular_bypass.html', {'form': form})


    




def get(request,page_name):
    
    #print(request.GET)
    #print(page_name)
    
    html_page = page_name + ".html"
    
    #return HttpResponse("<h1>mypage</h1>")
    return render(request, html_page, {})


def home(request):
    
    #print(request.GET)
    
    
    #return HttpResponse("<h1>Hello!</h1>")
    return render(request, 'home.html', {})

def favicon(request):
    return serve(request, 'img/cheers.png')