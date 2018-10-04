from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
	args={}
	if request.POST:
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('/main/',{'user':user})
	
		else:
			args['login_error']="Не правильный логин или пароль"
			return render(request,'accounts/login.html',args)
	else:
		return render(request,'accounts/login.html',args)			



def logout_user(request):
	logout(request)
	return redirect('/')		