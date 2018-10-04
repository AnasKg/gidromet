from django import template
from . import config
from calculation.models import Osadki
 
register = template.Library()


@register.simple_tag
def update_variable(value):
	config.f = value
	return ''

@register.simple_tag
def get_variable():
	return config.f

@register.simple_tag
def get_false():
	return config.f2	


@register.simple_tag
def queryQ():
	###day=str(val)
	###month=str(month)
	continueQuery='and month=%s' % 1
	mainQuery='SELECT otschot, date, extract(day from timestamp date) AS day, extract(month from timestamp date) as month, FROM calculation_osadki WHERE day=%s' % 3 % continueQuery
	have=Osadki.objects.raw(mainQuery)
	return have.otschot
	###for h in have
	###	if forloop.first
	###		return '1'