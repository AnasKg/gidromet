from django.shortcuts import render
from calculation.models import Osadki

# Create your views here.
def osadki(request):
	return render(request,'calculation/osadki.html',{'osadki':Osadki.objects.all(),'month':range(1,13),'days':range(1,32)})