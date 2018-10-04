from django.shortcuts import render
# Create your views here.
def main(request):
	return render(request,'main/homPage.html',{'user':request.user.get_username()})