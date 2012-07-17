# Create your views here.

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    form = LoginForm()
    if request.method == 'POST':
        #YOUR CODE HERE
        
	if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username, password)
            if user is not None:
                if user.is_active:
                    print "Correct user name and password"
                    return HttpResponseRedirect(request.path)
                else:
                    print "Your account has been disabled"
            else:
                print "Incorrect Username or password!!"
    
    
    return render_to_response('reg/login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated(),
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('reg/logout.html')
