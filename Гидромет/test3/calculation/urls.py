from django.urls import path
from . import views

urlpatterns = [
	path('osadki/',views.osadki,name='osadki'),
]