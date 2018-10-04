from django.db import models

# Create your models here.
class Akvatorii(models.Model):
	nameAkvatorii=models.CharField(max_length=100)
	changed=models.BooleanField()

	def __str__(self):
		return self.nameAkvatorii


class TochkiSbora(models.Model):
	name=models.CharField(max_length=150)
	longitude=models.CharField(max_length=200)
	latitude=models.CharField(max_length=200)
	stationType=models.CharField(max_length=100)
	status=models.BooleanField()
	otn=models.PositiveSmallIntegerField()
	akvatorii=models.ForeignKey(Akvatorii, on_delete=models.CASCADE)

	def __str__(self):
		return self.name	


class Type_Osadki(models.Model):
	nameOsadki=models.CharField(max_length=100)

	def __str__(self):
		return self.nameOsadki


class Osadki(models.Model):
	date=models.DateField()
	otschot=models.FloatField()
	popravka=models.FloatField()
	type_osadki=models.ForeignKey(Type_Osadki,on_delete=models.CASCADE)
	station=models.ForeignKey(TochkiSbora,on_delete=models.CASCADE)
	changed=models.BooleanField()

	def __str__(self):
		return str(self.date)

